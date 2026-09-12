#!/usr/bin/env python3
"""index.html이 참조하는 ./image 폴더 이미지를 base64로 치환해
index_single.html(이미지 내장 단일 파일)을 생성한다."""

import base64
import mimetypes
from pathlib import Path

BASE_DIR = Path(__file__).parent
SRC_HTML = BASE_DIR / "index.html"
OUT_HTML = BASE_DIR / "index_single.html"
IMAGE_DIR = BASE_DIR / "image"


def to_data_uri(path: Path) -> str:
    mime, _ = mimetypes.guess_type(path.name)
    mime = mime or "application/octet-stream"
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{data}"


def main():
    html = SRC_HTML.read_text(encoding="utf-8")
    image_files = sorted(IMAGE_DIR.glob("*.*"))
    if not image_files:
        raise SystemExit(f"이미지가 없습니다: {IMAGE_DIR}")

    for img_path in image_files:
        rel_path = f"./image/{img_path.name}"
        if rel_path not in html:
            continue
        html = html.replace(rel_path, to_data_uri(img_path))
        print(f"치환 완료: {rel_path} -> base64 ({img_path.stat().st_size:,} bytes)")

    OUT_HTML.write_text(html, encoding="utf-8")
    print(f"\n생성 완료: {OUT_HTML}")


if __name__ == "__main__":
    main()
