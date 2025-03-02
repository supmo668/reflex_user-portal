"""Template configuration for the application."""

from dataclasses import dataclass
from typing import List, Type

import reflex as rx

from ..backend.user_state import UserState
from ..models import UserType  # Import UserType from models


@dataclass
class NavItem:
    """Navigation item configuration."""

    title: str
    route: str
    icon: str
    requires_auth: bool = True  # Whether this item requires authentication
    admin_only: bool = False  # Whether this item is only for admins

    def should_show(self, state: Type[UserState]) -> rx.Var[bool]:
        """Check if this item should be shown based on auth state.

        Args:
            state: The user state class.

        Returns:
            A Var[bool] indicating if the item should be shown.
        """
        # For auth-required items, check auth and admin status
        return rx.cond(
            self.requires_auth,
            # Auth required
            rx.cond(
                self.admin_only,
                (state.current_user.user_type == UserType.ADMIN) & state.is_signed_in,  # Admin check
                state.is_signed_in,  # Regular auth is enough
            ),
            True,  # No auth required
        )


# Define all navigation items in specified order
NAV_ITEMS = [
    NavItem(
        title="About",
        route="/about",
        icon="info",
        requires_auth=False,  # Accessible to all
    ),
    NavItem(
        title="Profile",
        route="/profile",
        icon="user",
        requires_auth=True,
    ),
    NavItem(
        title="App Settings",
        route="/app-settings",
        icon="settings",
        requires_auth=False,
    ),
    NavItem(
        title="Admin Config",
        route="/admin/settings",
        icon="shield",
        requires_auth=True,
        admin_only=True,
    ),
    NavItem(
        title="User Management",
        route="/admin/users",
        icon="table",
        requires_auth=True,
        admin_only=True,
    ),
]
