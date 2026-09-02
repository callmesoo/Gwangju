# Gwangju

## WAV to Text 변환기

`wav_to_text.py`는 WAV 오디오 파일을 텍스트로 변환하는 CLI 도구입니다.

### 설치

```bash
pip install -r requirements.txt
```

whisper 엔진(오프라인 변환)을 사용하려면 추가로 설치하세요:

```bash
pip install openai-whisper
```

### 사용법

```bash
# Google Web Speech API 사용 (기본값, 인터넷 필요, API 키 불필요)
python wav_to_text.py audio.wav

# 오프라인 whisper 엔진 사용
python wav_to_text.py audio.wav --engine whisper

# 여러 파일을 변환하고 결과를 디렉터리에 저장
python wav_to_text.py *.wav --output-dir transcripts

# 언어 지정 (기본값: 한국어 ko-KR)
python wav_to_text.py audio.wav --language en-US
```

