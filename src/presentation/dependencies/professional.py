from application.use_cases.professional.check_professional_email import CheckProfessionalEmail
from application.use_cases.professional.confirm_email_change_for_professional import ConfirmEmailChange
from application.use_cases.professional.delete_professional import DeleteProfessionalAccount
from application.use_cases.professional.generate_register_verification_professional import GenerateRegisterVerificationProfessional
from application.use_cases.professional.get_professional import GetProfessional
from application.use_cases.professional.login_professional import LoginProfessional
from application.use_cases.professional.logout_professional import LogoutProfessional
from application.use_cases.professional.register_professional import RegisterProfessional
from application.use_cases.professional.request_password_reset_for_professional import RequestPasswordResetForProfessional
from application.use_cases.professional.reset_password_for_professional import ResetPassword
from application.use_cases.professional.send_email_to_change_email_for_professional import SendEmailToChangeEmailForProfessional
from application.use_cases.professional.update_professional_profile import UpdateProfessionalProfile

from infrastructure.database.repositories.appointment_repository import AppointmentRepositorySQLAlchemy
from infrastructure.database.repositories.availability_repository import AvailabilityRepositorySQLAlchemy
from infrastructure.database.repositories.professional_repository import ProfessionalRepositorySQLAlchemy
from infrastructure.database.repositories.refresh_token_repository import RefreshTokenRepositorySQLAlchemy

from infrastructure.security.password_hasher import PasswordHasher
from infrastructure.security.token_service import TokenService

from infrastructure.settings import settings

from domain.services.email_service import EmailService


def get_confirm_email_change_use_case() -> ConfirmEmailChange:
    return ConfirmEmailChange(
        professional_repository=ProfessionalRepositorySQLAlchemy(),
        refresh_token_repository=RefreshTokenRepositorySQLAlchemy(),
        token_service=TokenService(),
    )


def get_delete_professional_account_use_case() -> DeleteProfessionalAccount:
    return DeleteProfessionalAccount(
        professional_repository=ProfessionalRepositorySQLAlchemy(),
        appointment_repository=AppointmentRepositorySQLAlchemy(),
        availability_repository=AvailabilityRepositorySQLAlchemy(),
        refresh_token_repository=RefreshTokenRepositorySQLAlchemy(),
    )


def get_generate_register_verification_professional_account_use_case() -> GenerateRegisterVerificationProfessional:
    return GenerateRegisterVerificationProfessional(
        professional_repository=ProfessionalRepositorySQLAlchemy(),
        password_hasher=PasswordHasher(),
        email_service=EmailService(),
        frontend_base_url=settings.FRONTEND_BASE_URL,
    )


def get_professional_use_case() -> GetProfessional:
    return GetProfessional(
        professional_repository=ProfessionalRepositorySQLAlchemy(),
    )


def get_login_professional_use_case() -> LoginProfessional:
    return LoginProfessional(
        professional_repository=ProfessionalRepositorySQLAlchemy(),
        refresh_token_repository=RefreshTokenRepositorySQLAlchemy(),
        token_service=TokenService(),
        password_hasher=PasswordHasher(),
    )


def get_logout_professional_use_case() -> LogoutProfessional:
    return LogoutProfessional(
        professional_repository=ProfessionalRepositorySQLAlchemy(),
        refresh_token_repository=RefreshTokenRepositorySQLAlchemy(),
    )


def get_register_professional_use_case() -> RegisterProfessional:
    return RegisterProfessional(
        professional_repository=ProfessionalRepositorySQLAlchemy(),
        token_service=TokenService(),
    )


def get_request_password_reset_for_professional_use_case() -> RequestPasswordResetForProfessional:
    return RequestPasswordResetForProfessional(
        professional_repository=ProfessionalRepositorySQLAlchemy(),
        token_service=TokenService(),
        email_service=EmailService(),
    )


def get_reset_password_account_use_case() -> ResetPassword:
    return ResetPassword(
        professional_repository=ProfessionalRepositorySQLAlchemy(),
        refresh_token_repository=RefreshTokenRepositorySQLAlchemy(),
        token_service=TokenService(),
        password_hasher=PasswordHasher(),
    )


def get_send_email_to_change_email_for_professional_account_use_case() -> SendEmailToChangeEmailForProfessional:
    return SendEmailToChangeEmailForProfessional(
        professional_repository=ProfessionalRepositorySQLAlchemy(),
        token_service=TokenService(),
        email_service=EmailService(),
        frontend_base_url=settings.FRONTEND_BASE_URL,
    )


def get_update_professional_profile_account_use_case() -> UpdateProfessionalProfile:
    return UpdateProfessionalProfile(
        professional_repository=ProfessionalRepositorySQLAlchemy(),
    )


def get_check_professional_email_use_case() -> CheckProfessionalEmail:
    return CheckProfessionalEmail(
        professional_repository=ProfessionalRepositorySQLAlchemy(),
    )
