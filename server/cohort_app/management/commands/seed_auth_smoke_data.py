from django.core.management.base import BaseCommand
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from cohort_app.models import Cohort, ValidEmail

# python manage.py seed_auth_smoke_data --email 2017eerickson@gmail.com
class Command(BaseCommand):
    help = "Seed a cohort invite code and allowlisted email for auth smoke tests."

    def add_arguments(self, parser):
        parser.add_argument(
            "--invite-code",
            default="TEST-INVITE-123",
            help="Invite code to create or reuse.",
        )
        parser.add_argument(
            "--email",
            default="kamivision@gmail.com",
            help="Email to allowlist for the cohort.",
        )
        parser.add_argument(
            "--cohort-name",
            default="Smoke Test Cohort",
            help="Cohort name when creating a new cohort.",
        )

    def handle(self, *args, **options):
        invite_code = options["invite_code"].strip()
        email = options["email"].strip().lower()
        cohort_name = options["cohort_name"].strip()

        if not invite_code:
            self.stderr.write(self.style.ERROR("Invite code cannot be empty."))
            return

        if not cohort_name:
            self.stderr.write(self.style.ERROR("Cohort name cannot be empty."))
            return

        try:
            validate_email(email)
        except ValidationError:
            self.stderr.write(self.style.ERROR("Please provide a valid email address."))
            return

        cohort, cohort_created = Cohort.objects.get_or_create(
            invite_code=invite_code,
            defaults={"name": cohort_name},
        )

        valid_email, email_created = ValidEmail.objects.get_or_create(
            cohort=cohort,
            email=email,
        )

        if cohort_created:
            self.stdout.write(self.style.SUCCESS("Created cohort."))
        else:
            self.stdout.write("Reused existing cohort.")

        if email_created:
            self.stdout.write(self.style.SUCCESS("Added allowlisted email."))
        else:
            self.stdout.write("Allowlisted email already exists for this cohort.")

        self.stdout.write("---")
        self.stdout.write(f"cohort_id: {cohort.id}")
        self.stdout.write(f"cohort_name: {cohort.name}")
        self.stdout.write(f"invite_code: {cohort.invite_code}")
        self.stdout.write(f"email: {valid_email.email}")
