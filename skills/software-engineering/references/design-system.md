# Design-system playbook

Use this reference when a product needs a new visual language or when an existing UI is being made consistent. If a supplied design is locked, document its values and preserve them; do not replace them with this default system.

## Visual hierarchy

1. Establish one reading order per screen: page title, short context, primary action, content, secondary actions.
2. Use whitespace, alignment, and type scale before adding decoration. Avoid random cards, gradients, badges, or icons that do not encode meaning.
3. Give each screen one dominant action. Destructive actions must be separated, named clearly, and confirmed when needed.
4. Keep headings and navigation labels short. Use a longer supporting sentence only when it improves comprehension, onboarding, or legal accuracy.

## Semantic tokens

Define tokens once and consume them from components. Prefer semantic names over hue names so themes and brands can change without rewriting components.

| Token group | Minimum roles |
| --- | --- |
| Canvas/surface | `canvas`, `surface`, `surface-raised`, `surface-inverse` |
| Text | `text`, `text-muted`, `text-subtle`, `text-on-accent` |
| Borders | `border`, `border-strong`, `focus-ring` |
| Brand | `brand`, `brand-hover`, `brand-soft` |
| Status | `success`, `warning`, `danger`, `info` and readable soft variants |
| Effects | `shadow-sm`, `shadow-md`, `radius-sm`, `radius-md`, `radius-lg` |

When no brand is supplied, start with a calm neutral/white foundation, one distinctive accent, and status colors reserved for status. Define a dark theme by semantic role, not by simply inverting every RGB value. Check text and controls against WCAG contrast targets and check focus rings on both themes.

## Type and spacing

- Use at most two font families unless the brand requires more. Choose families with Arabic glyph coverage when Arabic is supported and verify Arabic shaping, diacritics, and numerals.
- Define a small type scale with explicit line heights for headings, body, labels, metadata, and code/numeric values. Avoid using font size as the only hierarchy signal.
- Use a consistent 4- or 8-unit spacing rhythm. Define container widths, page gutters, control heights, and table density as tokens.
- Keep line length readable on wide screens. Allow labels and error text to wrap instead of clipping or forcing horizontal scroll.

## Responsive behavior

Design behavior, not just breakpoints:

- **Phone:** single-column content, reachable primary action, bottom sheet/drawer for secondary navigation, touch targets at least 44 CSS pixels.
- **Tablet:** preserve the same information hierarchy while allowing two-column detail views when content remains readable.
- **Desktop:** constrain content width, use persistent navigation only when it adds value, and avoid filling empty space with decorative widgets.

Test at a narrow phone, a typical tablet, and a wide desktop. Check long titles, tables, forms, dialogs, file names, and validation messages at each size.

## Arabic, English, RTL, and LTR

- Keep translations in a locale layer; never concatenate translated fragments in components.
- Set document language and direction from the active locale. Mirror directional icons, breadcrumbs, chevrons, and asymmetric spacing, but do not mirror logos, media, or universally oriented symbols.
- Test mixed Arabic/English names, dates, phone numbers, decimals, and identifiers. Use logical CSS properties (`margin-inline`, `inset-inline`, `text-align: start`) where possible.
- Verify focus order and screen-reader order after direction changes. Do not rely on visual order alone.

## Themes and motion

- Store only the user's presentation preference in browser storage; the server remains authoritative for product data.
- Avoid flashes of the wrong theme by applying the theme before the first paint when the framework permits it.
- Use motion to explain state changes, not to decorate every interaction. Respect `prefers-reduced-motion`, provide a non-animated path, and never hide a status update behind animation.

## Component contract

Every shared component should define its supported states, keyboard behavior, accessible name, disabled/permission behavior, and theme/locale assumptions. Prefer composable primitives for buttons, inputs, select/combobox, tabs, tables, cards, dialogs, drawers, toasts, skeletons, empty states, and error boundaries. Keep domain data fetching in feature services or route loaders rather than inside generic visual primitives.

## Accessibility gate

Before calling the design complete, verify semantic landmarks, heading order, labels and descriptions, keyboard access, visible focus, contrast, error announcements, status announcements, reduced motion, zoom to 200%, and reflow without loss of content. Use icons as reinforcement, never as the only label.
