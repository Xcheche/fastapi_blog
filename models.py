from __future__ import annotations

from datetime import UTC, datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class User(Base):
    __tablename__ = "users"   # Django: class Meta: db_table = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    # Django: id = models.AutoField(primary_key=True)

    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    # Django: username = models.CharField(max_length=50, unique=True)

    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    # Django: email = models.EmailField(unique=True)

    image_file: Mapped[str | None] = mapped_column(String(200), nullable=True, default=None)
    # Django: image_file = models.CharField(max_length=200, null=True, blank=True)

    posts: Mapped[list["Post"]] = relationship(back_populates="author")
    # Django: related_name="posts" on ForeignKey in Post → one-to-many

    @property
    def image_path(self) -> str:
        # Django: define a model method for computed field
        if self.image_file:
            return f"/media/profile_pics/{self.image_file}"
        return "/static/profile_pics/default.jpg"


class Post(Base):
    __tablename__ = "posts"   # Django: class Meta: db_table = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    # Django: id = models.AutoField(primary_key=True)

    title: Mapped[str] = mapped_column(String(100), nullable=False)
    # Django: title = models.CharField(max_length=100)

    content: Mapped[str] = mapped_column(Text, nullable=False)
    # Django: content = models.TextField()

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
    # Django: author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    date_posted: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(UTC))
    # Django: date_posted = models.DateTimeField(auto_now_add=True)

    author: Mapped["User"] = relationship(back_populates="posts")
    # Django: implicit via ForeignKey(User, related_name="posts")
