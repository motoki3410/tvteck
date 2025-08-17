# TVTeck CLI システム

TVTeckのコマンドラインインターフェース（CLI）は、拡張可能なモジュラーアーキテクチャを採用しています。各機能カテゴリが独立したCLIクラスとして実装され、共通の基盤を提供するBaseCli基底クラスを継承しています。

## アーキテクチャ概要

### 主要コンポーネント

```
src/tvteck.py (メインエントリーポイント)
├── DeviceCli (device カテゴリ)
├── UpdateCli (update カテゴリ)
└── BaseCli (共通基底クラス)
```

### クラス階層

```
BaseCli (抽象基底クラス)
├── DeviceCli
└── UpdateCli
```

## BaseCli 基底クラス

すべてのCLIクラスは `BaseCli` を継承し、共通の機能を提供します。

### 主要メソッド

#### `_add_common_args(parser)`
すべてのコマンドに共通の引数を追加：
- `--param`: パラメータファイル指定

#### `_load_param(filepath)`
YAMLパラメータファイルを読み込み、該当カテゴリのパラメータを返す。

#### `_is_exist_args(args, req_args)`
必須引数の存在チェックを行い、不足している場合はエラーメッセージとヘルプを表示。

#### `_resolve_parameter(args, req_args)`
パラメータ解決の汎用ロジック：
1. `--param` オプションがある場合、YAMLファイルから読み込み
2. CLI引数から必須パラメータをチェック
3. パラメータオブジェクトを生成して返す

### 使用例

```python
class MyCli(BaseCli):
    def __init__(self):
        self.category = "mycategory"
        self.param_class = MyParameter
    
    def my_command(self, args):
        req_args = ["arg1", "arg2"]
        param = self._resolve_parameter(args, req_args)
        if not param:
            return
        # パラメータを使った処理
```

## カテゴリ実装

### DeviceCli

デバイス管理関連のコマンドを提供。

```bash
tvteck device <command> [options]
```

#### サポートコマンド

- `tmp`: 一時的なテストコマンド（開発用）

### UpdateCli

ファームウェアアップデート関連のコマンドを提供。

```bash
tvteck update <command> [options]
```

#### サポートコマンド

- `download`: ファームウェアダウンロード

#### downloadコマンド

ファームウェアのダウンロードを実行します。

```bash
# CLI引数による指定
tvteck update download --server example.com --url /path/to/firmware.bin

# パラメータファイルによる指定
tvteck update download --param data/update_param.yaml
```

**必須引数:**
- `--server`: ダウンロードサーバー
- `--url`: ファームウェアのURL

## パラメータシステム統合

各CLIコマンドは、以下の2つの方法でパラメータを受け取ることができます：

### 1. CLI引数による指定

```bash
tvteck update download --server example.com --url /firmware.bin
```

### 2. YAMLファイルによる指定

```bash
tvteck update download --param data/update_param.yaml
```

YAMLファイル例（`data/update_param.yaml`）:
```yaml
update:
  server: "example.com"
  url: "/firmware.bin"
```

### パラメータ解決の優先順位

1. `--param` オプションが指定された場合、YAMLファイルから読み込み
2. CLI引数から必要なパラメータを取得
3. 必須パラメータが不足している場合、エラーメッセージとヘルプを表示

## 新しいCLIカテゴリの追加

新しい機能カテゴリを追加するには、以下の手順を実行します：

### 1. CLIクラスの作成

```python
# src/mynew/mynew_cli.py
from base_cli import BaseCli
from mynew.mynew_parameter import MyNewParameter
from mynew.mynew import MyNew

class MyNewCli(BaseCli):
    def __init__(self):
        self.category = "mynew"
        self.mynew = MyNew()
        self.param_class = MyNewParameter

    def register(self, subparsers):
        parser = subparsers.add_parser(
            self.category,
            help="MyNew related commands"
        )
        self.cmd_sp = parser.add_subparsers(dest="command")
        
        common_parser = argparse.ArgumentParser(add_help=False)
        self._add_common_args(common_parser)
        
        self._register_mycommand(common_parser)
        parser.set_defaults(func=lambda args: parser.print_help())

    def _register_mycommand(self, common_parser):
        sp = self.cmd_sp.add_parser(
            "mycommand",
            help="My custom command",
            parents=[common_parser]
        )
        sp.add_argument("--arg1", help="First argument")
        sp.add_argument("--arg2", help="Second argument")
        sp.set_defaults(func=self.mycommand)

    def mycommand(self, args):
        req_args = ["arg1", "arg2"]
        param = self._resolve_parameter(args, req_args)
        if not param:
            return
        
        self.mynew.set_parameter(param)
        self.mynew.execute()
```

### 2. メインエントリーポイントへの登録

```python
# src/tvteck.py
from mynew.mynew_cli import MyNewCli

category_map = {
    "device": DeviceCli,
    "update": UpdateCli,
    "mynew": MyNewCli,  # 新しいカテゴリを追加
}
```

### 3. パラメータクラスの作成

```python
# src/mynew/mynew_parameter.py
from dataclasses import dataclass
from parameter.base_parameter import BaseParameter

@dataclass
class MyNewParameter(BaseParameter):
    arg1: str = ""
    arg2: str = ""
```

## コマンド例

### 基本使用

```bash
# ヘルプの表示
tvteck --help
tvteck device --help
tvteck update --help

# 特定コマンドのヘルプ
tvteck update download --help
```

### デバイス管理

```bash
# 一時テスト実行
tvteck device tmp
```

### アップデート管理

```bash
# ファームウェアダウンロード（CLI引数）
tvteck update download --server firmware.example.com --url /v1.0/firmware.bin

# ファームウェアダウンロード（パラメータファイル）
tvteck update download --param data/update_param.yaml
```

## エラーハンドリング

CLIシステムは以下のエラー状況を適切にハンドリングします：

### 必須引数不足

```bash
$ tvteck update download --server example.com
Missing arguments for download: url
```

この場合、エラーメッセージとコマンドのヘルプが自動的に表示されます。

### パラメータファイル不正

パラメータファイルが存在しない、または形式が不正な場合、ParameterManagerからのエラーメッセージが表示されます。

## 拡張ポイント

### カスタムバリデーション

各CLIクラスで独自のバリデーションロジックを実装できます：

```python
def _validate_parameters(self, param):
    if not param.server.startswith('https://'):
        print("Error: Server must use HTTPS")
        return False
    return True

def mycommand(self, args):
    param = self._resolve_parameter(args, ["server", "url"])
    if not param or not self._validate_parameters(param):
        return
    # 処理続行
```

### カスタムパラメータ処理

複雑なパラメータ変換が必要な場合、独自の処理を追加できます：

```python
def _post_process_parameters(self, param):
    # URL正規化
    if not param.url.startswith('/'):
        param.url = '/' + param.url
    return param
```

## ベストプラクティス

1. **一貫性**: 新しいコマンドも既存のパターンに従う
2. **ヘルプの充実**: 各コマンドに適切なヘルプメッセージを提供
3. **エラーメッセージ**: ユーザーが理解しやすいエラーメッセージ
4. **パラメータ設計**: YAMLファイルとCLI引数の両方をサポート
5. **テストカバレッジ**: 新しいコマンドには適切なテストを追加

## トラブルシューティング

### よくある問題

1. **コマンドが認識されない**
   - `category_map` に正しく登録されているか確認
   - import文が正しいか確認

2. **パラメータが解決されない**
   - `param_class` が正しく設定されているか確認
   - YAMLファイルの構造が正しいか確認

3. **必須引数エラーが発生する**
   - `req_args` リストと実際の引数名が一致しているか確認
   - `add_argument` での引数定義が正しいか確認
