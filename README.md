# 유민이 소개 페이지 배포 방법 (GitHub Pages)

1. `index.html`, `image` 폴더(1.jpg, 2.jpg 포함)를 수정했다면 `git add . && git commit -m "..." && git push`로 `main` 브랜치에 올리세요.
2. 저장소 **Settings → Pages**에서 Source가 `Deploy from a branch`, Branch가 `main` / `/(root)`로 설정되어 있으면 push 후 1~2분 내 자동 반영됩니다. (최초 설정 시에만 필요)
3. 배포된 링크(`https://enwise73.github.io/yumin-intro/`)를 카카오톡에 붙여넣으면 썸네일과 함께 공유됩니다. 미리보기가 안 뜨면 몇 분 후 다시 시도하거나 링크 뒤에 아무 문자나 붙여 새 링크로 공유해보세요.

## 참고: 사이트 주소가 바뀌면
`index.html`의 `SITE_URL`(head의 og:image·og:url 메타태그, `<script>`의 `CONFIG.SITE_URL`) 두 곳을 새 주소로 맞춘 뒤 다시 push하세요.
