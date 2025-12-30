# fastapi
from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.security import OAuth2PasswordRequestForm

# schemas
from application.schemas.professional import (
    DataToUpdate,
    DataToVerifyAccount,
    EmailData,
    ModifyPasswordData,
    ProfessionalEmailToUpdate,
    ResetPasswordData,
    Token,
)
from application.use_cases.professional.check_professional_email import (
    CheckProfessionalEmail,
)
from application.use_cases.professional.confirm_email_change_for_professional import (
    ConfirmEmailChange,
)
from application.use_cases.professional.delete_professional import (
    DeleteProfessionalAccount,
)

# use cases
from application.use_cases.professional.generate_register_verification_professional import (  # noqa: E501
    GenerateRegisterVerificationProfessional,
)
from application.use_cases.professional.get_professional import GetProfessional
from application.use_cases.professional.login_professional import LoginProfessional
from application.use_cases.professional.logout_professional import LogoutProfessional
from application.use_cases.professional.register_professional import (
    RegisterProfessional,
)
from application.use_cases.professional.request_password_reset_for_professional import (
    RequestPasswordResetForProfessional,
)
from application.use_cases.professional.reset_password_for_professional import (
    ResetPassword,
)
from application.use_cases.professional.send_email_to_change_email_for_professional import (  # noqa: E501
    SendEmailToChangeEmailForProfessional,
)
from application.use_cases.professional.update_professional_profile import (
    UpdateProfessionalProfile,
)

# entities
from domain.entities.professional import Professional

# dependencies
from presentation.dependencies.auth import get_current_professional
from presentation.dependencies.professional import (
    get_check_professional_email_use_case,
    get_confirm_email_change_use_case,
    get_delete_professional_account_use_case,
    get_generate_register_verification_professional_account_use_case,
    get_login_professional_use_case,
    get_logout_professional_use_case,
    get_professional_use_case,
    get_register_professional_use_case,
    get_request_password_reset_for_professional_use_case,
    get_reset_password_account_use_case,
    get_send_email_to_change_email_for_professional_account_use_case,
    get_update_professional_profile_account_use_case,
)

# settings
from infrastructure.settings import settings

router = APIRouter(prefix="/professional")


@router.post("/register/generate-verification-token")
async def generate_verification_token(
    data: DataToVerifyAccount,
    use_case: GenerateRegisterVerificationProfessional = Depends(
        get_generate_register_verification_professional_account_use_case
    ),
):
    await use_case.execute(data)

    return {"msg": "Email sent succesfully"}


@router.post("/register")
def register_professional(
    data: Token,
    use_case: RegisterProfessional = Depends(get_register_professional_use_case),
):
    use_case.execute(data.token)

    return {"msg": "Professional created successfully"}


@router.post("/login")
def login_professional(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    use_case: LoginProfessional = Depends(get_login_professional_use_case),
):
    try:
        result = use_case.execute(form_data.username, form_data.password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    response.set_cookie(
        key="refresh_token",
        value=result["refresh_token"],
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=60 * 60 * 48,  # 2 days
        path="/",
        domain=settings.FRONTEND_DOMAIN,
    )

    return {
        "access_token": result["access_token"],
        "token_type": "bearer",
        "expires_in": result["expires_in"],
    }


@router.get("/")
def get_professional_data_by_professional_id(
    current_professional: Professional = Depends(get_current_professional),
    use_case: GetProfessional = Depends(get_professional_use_case),
):
    response = use_case.get_by_id(current_professional.id)

    return response


@router.get("/{chat_code}")
def get_professional_data_by_chat_code(
    chat_code: str,
    use_case: GetProfessional = Depends(get_professional_use_case),
):
    response = use_case.get_by_chat_code(chat_code)

    return response


@router.post("/logout")
def logout(
    response: Response,
    request: Request,
    current_professional: Professional = Depends(get_current_professional),
    use_case: LogoutProfessional = Depends(get_logout_professional_use_case),
):
    refresh_token = request.cookies.get("refresh_token")
    use_case.execute(current_professional.id, refresh_token)

    response.delete_cookie(key="refresh_token", path="/", domain=settings.FRONTEND_DOMAIN)

    return {"msg": "Logout professional successfully"}


@router.delete("/delete")
def deleteAccount(
    response: Response,
    current_professional: Professional = Depends(get_current_professional),
    use_case: DeleteProfessionalAccount = Depends(
        get_delete_professional_account_use_case
    ),
):
    use_case.execute(current_professional.id)

    response.delete_cookie(key="refresh_token", path="/", domain=settings.FRONTEND_DOMAIN)

    return {"msg": "Professional successfully deleted."}


@router.get("/check-email/{email}")
def check_email(
    email: str,
    use_case: CheckProfessionalEmail = Depends(get_check_professional_email_use_case),
):
    result = use_case.execute(email)

    if result:
        return {"exists": True}
    else:
        return {"exists": False}


@router.put("/modify-data")
def modify_data(
    data_to_update: DataToUpdate,
    current_professional: Professional = Depends(get_current_professional),
    use_case: UpdateProfessionalProfile = Depends(
        get_update_professional_profile_account_use_case
    ),
):
    result = use_case.execute(
        professional_id=current_professional.id,
        name=data_to_update.name,
        profession=data_to_update.profession,
        profile_avatar_id=data_to_update.profile_avatar_id,
        phone_number=data_to_update.phone_number,
    )

    return result


@router.post("/send-email-to-change-email")
async def send_email_to_change_email(
    data: ProfessionalEmailToUpdate,
    current_professional: Professional = Depends(get_current_professional),
    use_case: SendEmailToChangeEmailForProfessional = Depends(
        get_send_email_to_change_email_for_professional_account_use_case
    ),
):
    await use_case.execute(current_professional.id, data.new_email)

    return {"msg": "Email sent successfully."}


@router.put("/confirm-email-modification")
def confirm_email_modification(
    data: Token,
    use_case: ConfirmEmailChange = Depends(get_confirm_email_change_use_case),
):
    use_case.execute(data.token)

    return {"msg": "Email changed succesfully."}


@router.post("/send-email-to-change-password")
async def forgot_your_password(
    email_data: EmailData,
    use_case: RequestPasswordResetForProfessional = Depends(
        get_request_password_reset_for_professional_use_case
    ),
):
    await use_case.execute(email_data.email)

    return {"msg": "Email sent successfully."}


@router.put("/confirm-password-modification")
async def reset_password(
    data: ResetPasswordData,
    use_case: ResetPassword = Depends(get_reset_password_account_use_case),
):
    use_case.without_login(data.token, data.new_password)

    return {"msg": "Password changed succesfully."}


@router.put("/modify-password-with-login")
def modify_password_with_login(
    data: ModifyPasswordData,
    current_professional: Professional = Depends(get_current_professional),
    use_case: ResetPassword = Depends(get_reset_password_account_use_case),
):
    use_case.with_login(
        professional_id=current_professional.id,
        old_password=data.old_password,
        new_password=data.new_password,
    )

    return {"msg": "Password changed succesfully."}
