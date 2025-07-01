from pydantic import BaseModel, Field
from typing import Annotated, List
from annotated_types import Len

class HeadWearInfo(BaseModel):
    type: str = Field(..., description="Tipo de protección en la cabeza: 'hard_hat', 'no_hard_hat', 'no_head_wear', 'unknown'.")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confianza de la detección del tipo de protección en la cabeza.")

class Detection(BaseModel):
    class_name: str = Field(..., description="Clase detectada por el modelo (e.g., 'person', 'hard_hat').")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confianza de la detección.")
    bbox: Annotated[List[float], Len(4)] = Field(..., description="Coordenadas del bounding box [x_min, y_min, x_max, y_max].")
    head_wear_info: HeadWearInfo = Field(None, description="Información específica sobre la protección en la cabeza si es una persona.")
    risk_associated: bool = Field(False, description="Indica si esta detección individual representa un riesgo.")
    # Si queréis las máscaras de segmentación en el JSON:
    # mask_polygon: List[List[float]] = Field(None, description="Lista de puntos [x, y] que forman el polígono de la máscara.")


class Summary(BaseModel):
    total_persons: int = Field(..., description="Número total de personas detectadas.")
    persons_with_hard_hat: int = Field(..., description="Número de personas detectadas con casco de seguridad.")
    persons_no_hard_hat: int = Field(..., description="Número de personas detectadas con algo en la cabeza pero no un casco de seguridad.")
    persons_no_head_wear: int = Field(..., description="Número de personas detectadas sin nada en la cabeza.")
    overall_risk_detected: bool = Field(..., description="True si se detectó al menos un riesgo en la imagen.")
    risk_details: str = Field(..., description="Descripción detallada de los riesgos detectados.")

class PredictionResponse(BaseModel):
    detections: List[Detection] = Field(..., description="Lista de todas las detecciones individuales.")
    summary: Summary = Field(..., description="Resumen general de las detecciones y el riesgo.")
    processed_image_base64: str = Field(..., description="Imagen original con los silueteados y etiquetas dibujadas, codificada en Base64 (data:image/png;base64,...).")