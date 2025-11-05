import requests
from typing import Optional

class ProfessorService:
    def __init__(self, base_url: str = "http://servico1:5000"):
        self.base_url = base_url

    def get_professor(self, professor_id: int) -> Optional[dict]:
        try:
            response = requests.get(f"{self.base_url}/professores/{professor_id}")

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                return None
            
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Erro ao comunicar com Serviço 1: {e}")

            return None