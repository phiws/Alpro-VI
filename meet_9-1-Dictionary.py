# Dictionary
# ? Struktur Data yang menampung 'key' dan 'value'
# ? {key: value}
# ? index -> key
# ? Apakah key = str ?? -> int str bool float
# ? Apakah value harus 1?? -> bebas

mahasiswa = {
    "nama": "Widi",
    "npm": 135,
    "asal": "Bali",
    # "ip" : 4.0
}

# ? Mengambil data pada dictionary
#! secara langsung
print(mahasiswa["npm"])
# print(mahasiswa["ip"]) #! should be error

#! dengan get()
print(f"Dengan get(): {mahasiswa.get('npm')}")
print(f"Dengan get('ip'): {mahasiswa.get('ip')}")
print(f"Dengan get('ip'), dengan default: {mahasiswa.get('ip','Key not found')}")

# ? Mengupdate/insert data ke dictionary
#! secara langsung
mahasiswa["nama"] = "Ilham"  # cara update
print(f"Update langsung: {mahasiswa}")
mahasiswa["ip"] = 4.0  # insert baru
print(f"Insert langsung: {mahasiswa}")

#! dengan update()
mahasiswa.update(
    {
        "npm": 101,
        "asal": "Ciamis",
    }
)
print(f"Update dengan update(): {mahasiswa}")
mahasiswa.update(
    {
        "hobi": ["ngoding", "membaca"],
        "dob": "13-08-2002",
    }
)
print(f"Insert dengan update(): {mahasiswa}")

#! dengna del
del mahasiswa["dob"]
print(f"Delete dengan del(): {mahasiswa}")

#! dengan pop()
mahasiswa.pop("ip")
print(f"Delete dengan pop(): {mahasiswa}")

#! popitem() -> menghapus item terakhir
mahasiswa.popitem()
print(f"Delete dengan popitem(): {mahasiswa}")

#! clear() -> menghapus semua data
mahasiswa.clear()
print(f"Delete semua dengan clear(): {mahasiswa}")