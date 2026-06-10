# Holmes

Situational awareness for your Home Assistant home: protocol composition,
device inventory (including non-HA hardware via nmap), health & critical
alerts, internet speed, a force-directed topology map with protocol and
electrical (breaker) lenses, and live activity — one panel, distinct from
HA's configuration pages. You configure the house elsewhere; Holmes observes it.

Pairs with [Wattson](https://github.com/jasonschulke/wattson) for the
electrical dimension — when Wattson is installed, Holmes gains a breaker lens
on the map, per-device breaker attribution, and panel-mapping progress.
Wattson maps the panel; Holmes watches the house.

## Install via HACS (custom repository)

1. HACS → ⋮ → **Custom repositories**
2. URL: `https://github.com/jasonschulke/holmes`, category: **Integration**. Add.
3. Find **Holmes** in HACS, **Download**, restart Home Assistant.
4. Settings → Devices & Services → **Add Integration** → **Holmes**.
5. **Holmes** appears in the sidebar.

## First open

Holmes connects over the Home Assistant WebSocket API. On first open, create a
long-lived access token (your profile → Security → Long-lived access tokens)
and paste it once per browser. (Roadmap: native panel auth, removing the token
step entirely.)

## Notes

- Manual devices and the seen-device memory are stored per-browser for now;
  moving them to HA storage is on the roadmap.
- Versioned via GitHub tags; HACS picks up new releases automatically.
