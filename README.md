# 텍스트 → PPT 변환기 / Text to PPT Converter

성경 구절 텍스트를 PowerPoint 슬라이드로 변환하는 웹 도구입니다.  
A web tool that converts Bible verse text into PowerPoint slides.

---

## 사용 방법 (한국어)

### 1. 파일 열기
`text_to_ppt.html` 파일을 브라우저에서 직접 열면 바로 사용할 수 있습니다. 별도의 설치나 서버가 필요하지 않습니다.

### 2. 텍스트 입력
- 텍스트 입력란에 성경 구절을 입력합니다.
- **첫 번째 줄**: 성경 구절 출처 (예: `요한복음 3:16`) — 슬라이드 **상단**에 표시됩니다.
- **두 번째 줄부터**: 본문 내용 — 슬라이드 **하단**에 표시됩니다.
- **빈 줄**: 빈 줄을 기준으로 새로운 슬라이드가 생성됩니다.
- 모든 텍스트는 **오른쪽 정렬**로 표시됩니다.

**입력 예시:**
```
요한복음 3:16
하나님이 세상을 이처럼 사랑하사
독생자를 주셨으니

시편 23:1
여호와는 나의 목자시니
내게 부족함이 없으리로다
```

### 3. 옵션 설정

| 설정 항목 | 설명 |
|---|---|
| 폰트 | 맑은 고딕, 굴림, 바탕, 나눔고딕 등 한글/영문 폰트 선택 |
| 줄 간격 | 1.0 (좁게) ~ 2.5 (매우 넓게) |
| 구절 글자 크기 | 성경 구절 출처의 글자 크기 (pt) |
| 본문 글자 크기 | 본문 내용의 글자 크기 (pt) |
| 구절 색상 | 성경 구절 출처의 글자 색상 |
| 본문 색상 | 본문 내용의 글자 색상 |
| 배경 이미지 | JPG/PNG 이미지를 배경으로 업로드 |
| 배경색 | 배경 이미지가 없을 때의 배경 색상 |

### 4. 미리보기
- 텍스트를 입력하면 오른쪽 미리보기 영역에 슬라이드가 실시간으로 표시됩니다.
- 슬라이드는 그리드 형태로 표시되어 전체 슬라이드를 한눈에 확인할 수 있습니다.
- 배경 이미지를 업로드하면 미리보기에도 즉시 반영됩니다.

### 5. PPT 다운로드
- **⬇ PPT 다운로드** 버튼을 클릭하면 `bible_slides.pptx` 파일이 저장됩니다.
- 16:9 와이드 비율 슬라이드로 생성됩니다.

---

## How to Use (English)

### 1. Open the File
Open `text_to_ppt.html` directly in your browser. No installation or server is required.

### 2. Enter Text
- Type your Bible verses into the text input area.
- **First line**: Bible verse reference (e.g., `John 3:16`) — displayed at the **top** of the slide.
- **Subsequent lines**: Verse body — displayed at the **bottom** of the slide.
- **Blank line**: A blank line creates a **new slide**.
- All text is **right-aligned**.

**Example input:**
```
John 3:16
For God so loved the world
that he gave his one and only Son

Psalm 23:1
The Lord is my shepherd
I lack nothing
```

### 3. Options

| Option | Description |
|---|---|
| Font | Choose from Korean and English fonts (Malgun Gothic, Gulim, Batang, NanumGothic, Arial, etc.) |
| Line Spacing | 1.0 (tight) to 2.5 (very loose) |
| Verse Font Size | Font size (pt) for the Bible reference line |
| Body Font Size | Font size (pt) for the verse body text |
| Verse Color | Text color for the Bible reference |
| Body Color | Text color for the verse body |
| Background Image | Upload a JPG/PNG image as the slide background |
| Background Color | Background color when no image is selected |

### 4. Preview
- Slides are rendered in real time as you type.
- All slides are displayed in a grid layout so you can see the full deck at a glance.
- Uploading a background image is immediately reflected in the preview.

### 5. Download PPT
- Click the **⬇ PPT Download** button to save `bible_slides.pptx`.
- Slides are generated in 16:9 widescreen format.

---

## 기술 스택 / Tech Stack

- **HTML / CSS / JavaScript** — 단일 파일, 프레임워크 없음 (Single file, no framework)
- **[PptxGenJS](https://gitbug.com/gitbrent/PptxGenJS)** v3.12 — 브라우저에서 직접 PPTX 파일 생성 (Client-side PPTX generation)
