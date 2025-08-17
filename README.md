# TVTeck

E2Eテストフレームワーク - モジュラーコンポーネント設計によるテスト自動化ツール

## 概要

TVTeckは、デバイス管理とパラメータ管理を中心とした、拡張可能なE2Eテストフレームワークです。YAMLベースの設定管理とdataclassによる型安全なパラメータシステムを提供し、各機能モジュールは独立して動作します。

## 機能

- **デバイス管理**: YAMLファイルベースのデバイス設定管理とCLIインターフェース
- **アップデート管理**: ファームウェアダウンロード等のアップデート機能
- **パラメータ管理**: dataclassベースの型安全なパラメータシステム
- **拡張可能なCLI**: モジュラー設計による柔軟なコマンドラインインターフェース
- **ライブラリユーティリティ**: YAML読み込み/書き込み機能
- **E2Eテストサポート**: テスト実行環境の基盤機能

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

### 依存関係

- Python >= 3.8
- PyYAML
- dacite

## 使用方法

### コマンドラインツール

TVTeckは拡張可能なCLIアーキテクチャを採用しており、カテゴリごとにコマンドが整理されています。

```bash
# ヘルプメッセージを表示
tvteck

# デバイス関連コマンド
tvteck device --help

# アップデート関連コマンド  
tvteck update --help

# デバイス一時テスト実行
tvteck device tmp

# ファームウェアダウンロード
tvteck update download --server example.com --url /firmware.bin

# パラメータファイルを使用したコマンド実行
tvteck device some-command --param data/sample_parameters.yaml
tvteck update download --param data/update_param.yaml

# 仮想環境を使用してコマンド実行
./bin/tvteck device tmp
./bin/tvteck update download --server example.com --url /firmware.bin
```

CLIシステムの詳細については、[CLIドキュメント](docs/cli.md)を参照してください。

### Python API

```python
from src.device.device import Device
from src.parameter.parameter_manager import ParameterManager
from src.lib.yaml_util import load_yaml, dump_yaml

# デバイス管理
device = Device()
device.load_device_file("sample_device.yaml")

# パラメータ管理
pm = ParameterManager()
pm.set_all_parameters()  # デフォルトパラメータ設定
pm.load_parameter_file("sample_parameters.yaml")  # YAMLから読み込み
pm.show_parameter()  # パラメータ表示

# YAML操作
data = load_yaml("config.yaml")
dump_yaml(data, "output.yaml")
```

## プロジェクト構造

```
tvteck/
├── src/
│   ├── __init__.py         # パッケージ初期化
│   ├── tvteck.py          # メインエントリーポイント（CLIハンドラー）
│   ├── constants.py       # 定数定義（空ファイル）
│   ├── device/            # デバイス管理モジュール
│   │   ├── device.py      # デバイス管理クラス
│   │   ├── device_cli.py  # デバイスCLIコマンド
│   │   └── device_parameter.py  # デバイスパラメータ定義
│   ├── parameter/         # パラメータ管理システム
│   │   ├── base_parameter.py     # パラメータ基底クラス
│   │   └── parameter_manager.py  # パラメータマネージャー
│   ├── lib/               # ユーティリティライブラリ
│   │   └── yaml_util.py   # YAML読み込み/書き込み
│   ├── update/            # アップデート管理
│   │   └── update_parameter.py   # アップデートパラメータ
│   ├── e2e_core/          # E2Eコア機能（開発中）
│   │   ├── client/        # クライアント実装
│   │   ├── server/        # サーバー実装
│   │   ├── job/           # ジョブ管理
│   │   └── ticket/        # チケット処理
│   ├── test_manager/      # テスト管理（開発中）
│   └── tracer/            # トレーシング機能（開発中）
├── data/                  # 設定データディレクトリ
│   ├── sample_parameters.yaml  # サンプルパラメータ
│   ├── dump_parameters.yaml    # パラメータダンプファイル
│   └── device/            # デバイス設定ファイル
│       └── sample_device.yaml  # サンプルデバイス設定
├── e2e_test/             # E2Eテストスイート
├── docs/                 # ドキュメント
│   ├── parameter.md      # パラメータシステム詳細ドキュメント
│   └── cli.md           # CLIシステム詳細ドキュメント
├── bin/                  # 実行可能スクリプト
│   ├── tvteck           # tvteckラッパースクリプト
│   └── screencap        # スクリーンキャプチャ（開発中）
├── scripts/             # セットアップスクリプト
│   └── setup.sh         # 開発環境セットアップ
├── pyproject.toml       # プロジェクト設定
├── requirements.txt     # 依存関係
└── README.md           # このファイル
```

## パラメータシステム

TVTeckは柔軟なパラメータ管理システムを提供します：

### 特徴

- **型安全**: dataclassベースの型定義
- **YAML連携**: 設定ファイルとの双方向変換
- **拡張可能**: 新しいパラメータタイプの簡単な追加
- **階層構造**: ネストしたパラメータ構造をサポート

### パラメータ例

```yaml
# data/sample_parameters.yaml
device:
  dsn: "test_device"
  project: "display"
  region: "1920x1080"
  config:
    test: "integration"
    update: true

update:
  update_frequency: 24
```

詳細については、[パラメータドキュメント](docs/parameter.md)を参照してください。

## CLIアーキテクチャ

TVTeckは拡張可能なCLIアーキテクチャを採用しています：

### 特徴

- **モジュラー設計**: カテゴリごとに独立したCLIクラス
- **共通インターフェース**: BaseCli継承による一貫性
- **パラメータ統合**: CLI引数とYAMLファイルの統合サポート
- **型安全なパラメータ**: dataclassベースのパラメータ解決

### サポートされているカテゴリ

- `device`: デバイス管理コマンド
- `update`: ファームウェアアップデート関連コマンド

CLIシステムの詳細については、[CLIドキュメント](docs/cli.md)を参照してください。

## 開発

### テスト実行

```bash
# 全テスト実行
pytest

# カバレッジ付きテスト
pytest --cov=src

# E2Eテスト実行
pytest e2e_test/
```

### コードフォーマット

```bash
# フォーマット実行
black src/

# リンティング
flake8 src/

# 型チェック
mypy src/
```

### 環境設定

```bash
# 開発環境セットアップ
./scripts/setup.sh

# 依存関係インストール
pip install -e .[dev]

# 仮想環境での実行
./bin/tvteck
```

## 設定

プロジェクトの設定は以下のファイルで管理されています：

- `pyproject.toml`: プロジェクト設定とビルド設定、依存関係
- `src/constants.py`: アプリケーション定数（現在は空）
- `data/*.yaml`: パラメータとデバイス設定ファイル

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