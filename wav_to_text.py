#!/usr/bin/env python3
"""WAV 오디오 파일을 텍스트로 변환하는 CLI 도구.

두 가지 변환 엔진을 지원한다:
  - google  : SpeechRecognition + Google Web Speech API (인터넷 필요, API 키 불필요)
  - whisper : OpenAI Whisper (오프라인, 별도 설치 필요: pip install openai-whisper)

사용 예:
  python wav_to_text.py audio.wav
  python wav_to_text.py audio.wav --engine whisper --language ko
  python wav_to_text.py *.wav --output-dir transcripts
"""

import argparse
import sys
from pathlib import Path


def transcribe_google(wav_path: Path, language: str) -> str:
    import speech_recognition as sr

    recognizer = sr.Recognizer()
    with sr.AudioFile(str(wav_path)) as source:
        audio = recognizer.record(source)
    return recognizer.recognize_google(audio, language=language)


def transcribe_whisper(wav_path: Path, language: str, model_size: str) -> str:
    import whisper

    model = whisper.load_model(model_size)
    result = model.transcribe(str(wav_path), language=language)
    return result["text"].strip()


def transcribe(wav_path: Path, engine: str, language: str, model_size: str) -> str:
    if engine == "google":
        return transcribe_google(wav_path, language)
    if engine == "whisper":
        # whisper는 "ko", "en" 같은 짧은 코드를 쓰고, google은 "ko-KR" 같은 로케일을 쓴다.
        whisper_lang = language.split("-")[0]
        return transcribe_whisper(wav_path, whisper_lang, model_size)
    raise ValueError(f"알 수 없는 엔진: {engine}")


def main() -> int:
    parser = argparse.ArgumentParser(description="WAV 파일을 텍스트로 변환합니다.")
    parser.add_argument("files", nargs="+", help="변환할 .wav 파일 경로 (여러 개 가능)")
    parser.add_argument(
        "--engine",
        choices=["google", "whisper"],
        default="google",
        help="사용할 음성 인식 엔진 (기본값: google)",
    )
    parser.add_argument(
        "--language",
        default="ko-KR",
        help="인식할 언어 (기본값: ko-KR, whisper 사용 시 자동으로 'ko'로 변환됨)",
    )
    parser.add_argument(
        "--model-size",
        default="base",
        choices=["tiny", "base", "small", "medium", "large"],
        help="whisper 엔진 사용 시 모델 크기 (기본값: base)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="결과 .txt 파일을 저장할 디렉터리 (지정하지 않으면 표준 출력에만 출력)",
    )
    args = parser.parse_args()

    if args.output_dir:
        args.output_dir.mkdir(parents=True, exist_ok=True)

    exit_code = 0
    for file_arg in args.files:
        wav_path = Path(file_arg)
        if not wav_path.exists():
            print(f"[오류] 파일을 찾을 수 없습니다: {wav_path}", file=sys.stderr)
            exit_code = 1
            continue

        try:
            text = transcribe(wav_path, args.engine, args.language, args.model_size)
        except Exception as exc:  # noqa: BLE001 - CLI 도구이므로 모든 실패를 사용자에게 보여준다
            print(f"[오류] {wav_path} 변환 실패: {exc}", file=sys.stderr)
            exit_code = 1
            continue

        print(f"=== {wav_path} ===")
        print(text)

        if args.output_dir:
            out_path = args.output_dir / (wav_path.stem + ".txt")
            out_path.write_text(text, encoding="utf-8")
            print(f"-> 저장됨: {out_path}")

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
