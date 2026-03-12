# Text → PPT Converter

A browser-based tool that instantly converts text into a PowerPoint (.pptx) file.

---

## Getting Started

No installation required. Open `text_to_ppt.html` directly in any modern browser.

---

## Features

### Slide Content
- **Presentation Title**: The first line of text is used as the global title, displayed in the top-right corner of the first slide only.
- **Slide Body**: Separate slides by a blank line. Each block of text becomes one slide.

### Text Style
- **Font**: Choose from 10 typefaces — Malgun Gothic, NanumGothic, NanumMyeongjo, Arial, Calibri, Times New Roman, Georgia, Verdana, Trebuchet MS, Comic Sans MS
- **Font Size**: Adjustable from 16pt to 72pt via slider
- **Line Spacing**: Adjustable from 1.0× to 3.0× via slider
- **Font Color**: Color picker or quick presets (white, black, yellow, sky blue, red, green, purple)
- **Text Alignment**: Left / Center / Right

### Background
- **Gradient Presets**: 12 color combinations, applied with a single click
- **Solid Color**: Color picker or preset swatches
- **Background Image**: Upload one or multiple image files
  - Single image → applied to all slides
  - Multiple images → rotate through images per slide (cycle mode)
  - Remove images with the "✕ Remove Image" button

### Slide Size
| Option | Ratio |
|--------|-------|
| Widescreen (default) | 16:9 |
| Standard | 4:3 |
| Widescreen+ | 16:10 |

### Live Preview
- The right panel updates in real time as you type or change any setting.
- Background images, text styles, and body content are all reflected.

### PPT Download
- Click **⬇ Download PPT** to generate and save `슬라이드.pptx`.
- Text alignment, line spacing, background images, and drop shadows are all preserved in the exported file.

---

## Tech Stack

- **pptxgenjs 3.12** — generates .pptx files directly in the browser
- Plain HTML / CSS / JavaScript — no external frameworks
