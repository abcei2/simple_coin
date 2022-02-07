from django.db import models
import uuid
import hashlib
from typing import Dict, Any
from django.conf import settings

def get_short_uuid(uuid) -> str:
    """get the first block of a 4-word UUID to use as a short identifier"""
    full_uuid = str(uuid)
    return full_uuid.split("-", 1)[0]

# Create your models here.

class Transaction(models.Model):
    reference = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ammount_in_cents = models.FloatField()
    coin_type = models.CharField(max_length=64,default="COP")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def short_id(self) -> str:
        return get_short_uuid(self.reference)
    
    @property
    def signature_integrity(self) -> str:
        # Ejemplo

        concat_str = f"{self.reference}{int(self.ammount_in_cents)}{self.coin_type}{settings.WOMPI_PUBLIC_KEY}"

        print(concat_str)
        m = hashlib.sha256(concat_str.encode("utf8"))
        hashed = m.hexdigest()
        print(hashed)
        return  hashed

