# TVTeck

E2Eテストフレームワーク - モジュラーコンポーネント設計によるテスト自動化ツール

## 概要

TVTeckは、デバイス管理、トレーシング、ジョブ管理などの機能を独立したモジュールとして提供するE2Eテストフレームワークです。各モジュールは単独で動作し、統一的なテストインターフェースを通じてアクセス可能です。

## 機能

- **デバイス管理**: テスト対象デバイスの制御と監視
- **E2Eコア**: クライアント-サーバー通信、ジョブ管理、チケット処理
- **トレーシング**: テスト実行時の詳細ログとトレース機能
- **テストマネージャー**: テストスイートの統合管理
- **スクリーンキャプチャ**: 自動画面キャプチャ機能

## インストール

### 開発環境のセットアップ

```bash
git clone https://github.com/motoki3410/tvteck.git
cd tvteck
pip install -e .[dev]
```

### 基本インストール

```bash
pip install tvteck
```

## 使用方法

### コマンドラインツール

```bash
# メインコマンド
tvteck

# スクリーンキャプチャ
./bin/screencap

# KPI測定
./bin/tvteckkpi
```

### Python API

```python
from tvteck.device import DeviceManager
from tvteck.e2e_core.client import Client
from tvteck.tracer import Tracer

# デバイス管理
device_manager = DeviceManager()
device_manager.initialize()

# クライアント接続
client = Client()
client.connect()

# トレーシング開始
tracer = Tracer()
tracer.start_trace()
```

## プロジェクト構造

```
tvteck/
├── src/
│   ├── tvteck.py           # メインエントリーポイント
│   ├── constants.py        # 定数定義
│   ├── parameter.py        # パラメータ管理
│   ├── device/             # デバイス管理モジュール
│   ├── e2e_core/          # E2Eコア機能
│   │   ├── client/        # クライアント実装
│   │   ├── server/        # サーバー実装
│   │   ├── job/           # ジョブ管理
│   │   └── ticket/        # チケット処理
│   ├── lib/               # ユーティリティライブラリ
│   ├── test_manager/      # テスト管理
│   ├── tracer/            # トレーシング機能
│   └── update/            # アップデート管理
├── tests/                 # テストスイート
├── bin/                   # 実行可能スクリプト
├── docs/                  # ドキュメント
└── scripts/               # セットアップスクリプト
```

## 開発

### テスト実行

```bash
# 全テスト実行
pytest

# カバレッジ付きテスト
pytest --cov=src

# 特定のモジュールのテスト
pytest tests/test_device.py
```

### コードフォーマット

```bash
# フォーマット実行
black src/ tests/

# リンティング
flake8 src/ tests/

# 型チェック
mypy src/
```

### 環境設定

```bash
# 開発環境セットアップ
./scripts/setup.sh
```

## 設定

プロジェクトの設定は以下のファイルで管理されています：

- `pyproject.toml`: プロジェクト設定とビルド設定
- `src/constants.py`: アプリケーション定数
- `src/parameter.py`: パラメータ設定

## 貢献

1. このリポジトリをフォーク
2. 機能ブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

## ライセンス

このプロジェクトのライセンスについては、LICENSEファイルを参照してください。

## 作者

motoki3410

## 課題・質問

課題や質問がある場合は、[Issues](https://github.com/motoki3410/tvteck/issues)セクションで報告してください。