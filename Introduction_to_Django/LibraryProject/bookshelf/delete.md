```
from bookshelf.models import book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Book.objects.all()
```
