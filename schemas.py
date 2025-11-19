"""
Database Schemas for Vet Clinic

Each Pydantic model represents a MongoDB collection.
Collection name is the lowercase of the class name.
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class PetOwner(BaseModel):
    full_name: str = Field(..., description="Owner full name")
    email: str = Field(..., description="Owner email")
    phone: str = Field(..., description="Contact phone number")
    address: Optional[str] = Field(None, description="Street address")


class Pet(BaseModel):
    owner_id: Optional[str] = Field(None, description="Reference to PetOwner _id as string")
    name: str = Field(..., description="Pet name")
    species: str = Field(..., description="Species, e.g., Dog, Cat")
    breed: Optional[str] = Field(None, description="Breed")
    age_years: Optional[float] = Field(None, ge=0, description="Age in years")
    notes: Optional[str] = Field(None, description="Medical notes or preferences")


class Appointment(BaseModel):
    owner_name: str = Field(..., description="Owner full name")
    owner_email: str = Field(..., description="Owner email")
    owner_phone: str = Field(..., description="Owner phone")
    pet_name: str = Field(..., description="Pet name")
    pet_species: str = Field(..., description="Pet species")
    reason: str = Field(..., description="Visit reason")
    preferred_date: str = Field(..., description="Preferred date (string)")
    preferred_time: str = Field(..., description="Preferred time (string)")
    status: str = Field("pending", description="Appointment status: pending/confirmed/cancelled")


class ContactMessage(BaseModel):
    name: str = Field(..., description="Sender name")
    email: str = Field(..., description="Sender email")
    message: str = Field(..., description="Message body")
    subject: Optional[str] = Field("General Inquiry", description="Message subject")


# Example schemas preserved for reference (not used by the clinic app)
class User(BaseModel):
    name: str
    email: str
    address: str
    age: Optional[int] = Field(None, ge=0, le=120)
    is_active: bool = True


class Product(BaseModel):
    title: str
    description: Optional[str] = None
    price: float = Field(..., ge=0)
    category: str
    in_stock: bool = True
