from django import forms
from django import forms
from wishlist.models import BarangWishlist

class taskform(forms.ModelForm):
    class Meta:
        model = BarangWishlist
        fields = {"nama_barang", "harga_barang", "deskripsi"}