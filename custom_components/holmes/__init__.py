"""Holmes — device & network situational-awareness panel for Home Assistant."""
from __future__ import annotations

from pathlib import Path

from homeassistant.components import frontend
from homeassistant.components.http import StaticPathConfig
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN, PANEL_URL_PATH, URL_BASE


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Serve the app and register the sidebar panel."""
    if not hass.data.get(DOMAIN, {}).get("static_registered"):
        await hass.http.async_register_static_paths(
            [
                StaticPathConfig(
                    URL_BASE,
                    str(Path(__file__).parent / "frontend"),
                    cache_headers=False,
                )
            ]
        )
        hass.data.setdefault(DOMAIN, {})["static_registered"] = True

    frontend.async_register_built_in_panel(
        hass,
        "iframe",
        sidebar_title="Holmes",
        sidebar_icon="mdi:magnify-scan",
        frontend_url_path=PANEL_URL_PATH,
        config={"url": f"{URL_BASE}/holmes.html"},
        require_admin=False,
    )
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Remove the panel on unload."""
    frontend.async_remove_panel(hass, PANEL_URL_PATH)
    return True
