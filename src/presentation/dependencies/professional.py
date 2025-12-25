from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db


# use cases
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

# repositories of the database
from infrastructure.database.repositories.appointment_repository import AppointmentRepositorySQLAlchemy
from infrastructure.database.repositories.availability_repository import AvailabilityRepositorySQLAlchemy
from infrastructure.database.repositories.professional_repository import ProfessionalRepositorySQLAlchemy
from infrastructure.database.repositories.refresh_token_repository import RefreshTokenRepositorySQLAlchemy

# JWT
from infrastructure.security.password_hasher import PasswordHasher
from infrastructure.security.token_service import TokenService

# settings of the env
from infrastructure.settings import settings

# email service
from infrastructure.email.fastapi_mail_service import FastAPIMailService


def get_confirm_email_change_use_case(
    db: Session = Depends(get_db)
) -> ConfirmEmailChange:
    return ConfirmEmailChange(
        professional_repository=ProfessionalRepositorySQLAlchemy(db),
        refresh_token_repository=RefreshTokenRepositorySQLAlchemy(db),
        token_service=TokenService(),
    )


def get_delete_professional_account_use_case(
    db: Session = Depends(get_db)
) -> DeleteProfessionalAccount:
    return DeleteProfessionalAccount(
        professional_repository=ProfessionalRepositorySQLAlchemy(db),
        appointment_repository=AppointmentRepositorySQLAlchemy(db),
        availability_repository=AvailabilityRepositorySQLAlchemy(db),
        refresh_token_repository=RefreshTokenRepositorySQLAlchemy(db),
    )


def get_generate_register_verification_professional_account_use_case(
    db: Session = Depends(get_db)
) -> GenerateRegisterVerificationProfessional:
    return GenerateRegisterVerificationProfessional(
        professional_repository=ProfessionalRepositorySQLAlchemy(db),
        password_hasher=PasswordHasher(),
        token_service=TokenService(),
        email_service=FastAPIMailService(),
        frontend_base_url=settings.FRONTEND_BASE_URL,
    )


def get_professional_use_case(
    db: Session = Depends(get_db)
) -> GetProfessional:
    return GetProfessional(
        professional_repository=ProfessionalRepositorySQLAlchemy(db),
    )


def get_login_professional_use_case(
    db: Session = Depends(get_db)
) -> LoginProfessional:
    return LoginProfessional(
        professional_repository=ProfessionalRepositorySQLAlchemy(db),
        refresh_token_repository=RefreshTokenRepositorySQLAlchemy(db),
        token_service=TokenService(),
        password_hasher=PasswordHasher(),
    )


def get_logout_professional_use_case(
    db: Session = Depends(get_db)
) -> LogoutProfessional:
    return LogoutProfessional(
        professional_repository=ProfessionalRepositorySQLAlchemy(db),
        refresh_token_repository=RefreshTokenRepositorySQLAlchemy(db),
    )


def get_register_professional_use_case(
    db: Session = Depends(get_db)
) -> RegisterProfessional:
    return RegisterProfessional(
        professional_repository=ProfessionalRepositorySQLAlchemy(db),
        token_service=TokenService(),
    )


def get_request_password_reset_for_professional_use_case(
    db: Session = Depends(get_db)
) -> RequestPasswordResetForProfessional:
    return RequestPasswordResetForProfessional(
        professional_repository=ProfessionalRepositorySQLAlchemy(db),
        token_service=TokenService(),
        email_service=FastAPIMailService(),
    )


def get_reset_password_account_use_case(
    db: Session = Depends(get_db)
) -> ResetPassword:
    return ResetPassword(
        professional_repository=ProfessionalRepositorySQLAlchemy(db),
        refresh_token_repository=RefreshTokenRepositorySQLAlchemy(db),
        token_service=TokenService(),
        password_hasher=PasswordHasher(),
    )


def get_send_email_to_change_email_for_professional_account_use_case(
    db: Session = Depends(get_db)
) -> SendEmailToChangeEmailForProfessional:
    return SendEmailToChangeEmailForProfessional(
        professional_repository=ProfessionalRepositorySQLAlchemy(db),
        token_service=TokenService(),
        email_service=FastAPIMailService(),
        frontend_base_url=settings.FRONTEND_BASE_URL,
    )


def get_update_professional_profile_account_use_case(
    db: Session = Depends(get_db)
) -> UpdateProfessionalProfile:
    return UpdateProfessionalProfile(
        professional_repository=ProfessionalRepositorySQLAlchemy(db),
    )


def get_check_professional_email_use_case(
    db: Session = Depends(get_db)
) -> CheckProfessionalEmail:
    return CheckProfessionalEmail(
        professional_repository=ProfessionalRepositorySQLAlchemy(db),
    )
