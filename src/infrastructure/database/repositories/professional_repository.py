from sqlalchemy.orm import Session

from domain.entities.professional import Professional
from domain.repositories.professional_repository import ProfessionalRepository
from infrastructure.database.models.professional import ProfessionalModel


class ProfessionalRepositorySQLAlchemy(ProfessionalRepository):

    def __init__(self, session: Session):
        self.session = session
    
    def exists_by_email(self, email: str) -> bool:
        return (
            self.session.query(ProfessionalModel).filter(ProfessionalModel.email == email).first()
            is not None
        )

    def get_by_id(self, professional_id: int) -> Professional | None:
        model = (
            self.session.query(ProfessionalModel)
            .filter(ProfessionalModel.id == professional_id)
            .first()
        )

        if not model:
            return None

        return self._to_entity(model)

    def get_by_email(self, email: str) -> Professional | None:
        model = (
            self.session.query(ProfessionalModel)
            .filter(ProfessionalModel.email == email)
            .first()
        )

        if not model:
            return None

        return self._to_entity(model)
    
    def get_by_chat_code(self, chat_code: str) -> Professional | None:
        model = (
            self.session.query(ProfessionalModel)
            .filter(ProfessionalModel.chat_code == chat_code)
            .first()
        )

        if not model:
            return None

        return self._to_entity(model)

    def save(self, professional: Professional) -> None:
        model = ProfessionalModel(
            profile_avatar_id=professional.profile_avatar_id,
            name=professional.name,
            hashed_password=professional.hashed_password,
            email=professional.email,
            profession=professional.profession,
            phone_number=professional.phone_number,
            chat_code=professional.chat_code,
            status=professional.status,
        )

        self.session.add(model)
        self.session.commit()

    def delete(self, professional_id: int) -> None:
        self.session.query(ProfessionalModel).filter_by(
            id=professional_id
        ).delete()
        self.session.commit()

    def _to_entity(self, model: ProfessionalModel) -> Professional:
        return Professional(
            id=model.id,
            profile_avatar_id=model.profile_avatar_id,
            name=model.name,
            hashed_password=model.hashed_password,
            email=model.email,
            profession=model.profession,
            phone_number=model.phone_number,
            chat_code=model.chat_code,
            status=model.status,
        )
