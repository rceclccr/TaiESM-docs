# TaiESM Documentation

本倉庫提供 **TaiESM**（臺灣地球系統模式）之文件來源。Read the Docs 會從不同分支建置對應版本的網站。

- 主要網站（建置成功後）：`https://taiesm-docs.readthedocs.io/en/latest/`
- 如何編輯：在網站頁面點選 "Edit on GitHub" 或直接對應檔案送 PR。

## 本機預覽
```bash
pip install -r requirements.txt
sphinx-build . _build
open _build/index.html
```

## 分支與版本建議
- `main`：最新文件（可能對應開發版本）
- `taiesm1`、`taiesm2`：各版本對應之文件
- 標籤（tags）：發行版（例如 `v2.0.0`）
