"""Authentication pages using Clerk."""

import reflex as rx
import reflex_clerk as clerk
import os

from reflex_user_portal.backend.user_state import UserState


def profile_content() -> rx.Component:
    """Profile page content showing user information.

    Returns:
        The profile page content.
    """
    return rx.vstack(
        rx.heading("Profile", size="5"),
        rx.cond(
            clerk.ClerkState.is_signed_in,
            rx.vstack(
                 rx.flex(
                    clerk.user_button(),
                    width="100%",
                    spacing="7",
                    margin_top="0.75rem",
                    padding_right="0.75rem",
                    direction="column",
                    align="end",
                ),
                rx.cond(
                    clerk.ClerkState.user.has_image,
                    rx.avatar(
                        src=clerk.ClerkState.user.image_url,
                        name=clerk.ClerkState.user.first_name,
                        size="3",
                    ),
                    rx.avatar(
                        name=clerk.ClerkState.user.first_name,
                        size="3",
                    ),
                ),
                rx.vstack(
                    rx.text("Name", weight="bold"),
                    rx.cond(
                        (clerk.ClerkState.user.first_name != "") & (clerk.ClerkState.user.last_name != ""),
                        rx.text(clerk.ClerkState.user.first_name + " " + clerk.ClerkState.user.last_name),
                        rx.text("Not provided"),
                    ),
                    border="1px solid var(--gray-200)",
                    border_radius="md",
                    padding="4",
                ),
                rx.vstack(
                    rx.text("Email", weight="bold"),
                    rx.foreach(
                        clerk.ClerkState.user.email_addresses,
                        lambda email: rx.text(email.email_address),
                    ),
                    border="1px solid var(--gray-200)",
                    border_radius="md",
                    padding="4",
                ),
                rx.vstack(
                    rx.text("Role", weight="bold"),
                    rx.text(UserState.user_role),
                    border="1px solid var(--gray-200)",
                    border_radius="md",
                    padding="4",
                ),
                clerk.signed_out(
                    rx.button(
                        clerk.sign_in_button(),
                        size="3",
                        color_scheme="gray",
                        background="black"
                    ),
                ),
                clerk.signed_in(
                    rx.button(
                        clerk.sign_out_button(),
                        size="3",
                        color_scheme="gray",
                        background="black"
                    )
                ),
                width="100%",
                max_width="400px",
                spacing="4",
                align_items="center",
            ),
            rx.text("You are not signed in.", size="3"),
        ),
        spacing="8",
        width="100%",
    )
