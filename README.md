# Gwangju

## WAV to Text 변환기

`wav_to_text.py`는 WAV 오디오 파일을 텍스트로 변환하는 CLI 도구입니다.

### 설치

```bash
pip install -r requirements.txt
```

기본 엔진인 whisper는 시스템에 `ffmpeg`가 설치되어 있어야 합니다 (예: `apt install ffmpeg`, `brew install ffmpeg`).

Google Web Speech API 엔진(온라인)을 사용하려면 `requirements.txt`에서 `SpeechRecognition` 줄의 주석을 해제한 뒤 설치하세요. 다만 이는 비공식 무료 엔드포인트라 최근 `Bad Request` 오류로 자주 실패하니, 특별한 이유가 없다면 기본값인 whisper 사용을 권장합니다.

### 사용법

```bash
# 오프라인 whisper 엔진 사용 (기본값)
python wav_to_text.py audio.wav

# whisper 모델 크기 지정 (tiny/base/small/medium/large, 기본값: base)
python wav_to_text.py audio.wav --model-size small

# Google Web Speech API 사용 (인터넷 필요, 비공식 API라 불안정할 수 있음)
python wav_to_text.py audio.wav --engine google

# 여러 파일을 변환하고 결과를 디렉터리에 저장
python wav_to_text.py *.wav --output-dir transcripts

# 언어 지정 (기본값: 한국어 ko-KR)
python wav_to_text.py audio.wav --language en-US
```

