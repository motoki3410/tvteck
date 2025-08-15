# パラメータ管理の仕組み

## 概要

TVTeckプロジェクトでは、テストや各種処理で利用する設定値（パラメータ）を一元管理するために `ParameterManager` クラスを用意しています。
パラメータはカテゴリごと（例: device, update）にdataclassとして定義され、柔軟かつ拡張性の高い設計となっています。

---

## 主な構成

### BaseParameter（基底クラス）

全パラメータクラスの基底クラスとして機能し、共通メソッドを提供：

```python
@dataclass
class BaseParameter:
    def get_field_names(self):  # フィールド名のリストを取得
    def dump_parameter(self):   # 辞書形式でパラメータを出力
```

### パラメータクラス

BaseParameterを継承したdataclassとして定義：

```python
@dataclass
class DeviceParameter(BaseParameter):
    dsn: str = "jp_device_1"
    project: str = "wyoming"
    region: str = "jp"
    config: DeviceConfig = None  # ネストした構造も可能
```

### ParameterManager

- パラメータカテゴリとクラスのマッピング（`param_map`）を保持
- 各カテゴリのパラメータインスタンスを `self.parameters` で管理
- YAMLファイルからの読み込み・書き込み機能を提供

#### 主なメソッド

| メソッド名 | 役割 |
|------------|------|
| `set_parameter(name, param)` | 指定カテゴリにパラメータインスタンスをセット |
| `set_all_parameters()` | 全カテゴリのパラメータをデフォルト値で初期化 |
| `get_field_names(category)` | 指定カテゴリのフィールド名一覧を取得 |
| `get_all_category_field_names()` | 全カテゴリのフィールド名一覧を取得 |
| `load_parameter_file(filename)` | YAMLファイルからパラメータを読み込み |
| `dump_parameter_file(filename)` | パラメータをYAMLファイルに書き出し |
| `show_parameter()` | 全パラメータの内容を表示 |

---

## YAMLファイル連携

### 読み込み例（sample_parameters.yaml）

```yaml
device:
  dsn: "test_device_1"
  project: "test_project"
  region: "us"
  config:
    test: "integration"
    update: true
update:
  name: "firmware_update"
  version: "v2.0.0"
```

### 使用方法

```python
pm = ParameterManager()
pm.load_parameter_file("sample_parameters.yaml")  # YAMLから読み込み
pm.show_parameter()                               # パラメータ表示
pm.dump_parameter_file("output.yaml")            # YAMLに書き出し
```

---

## 拡張方法

1. 新しいパラメータクラスを作成（BaseParameterを継承）
2. `param_map` に追加
3. 対応するYAMLセクションを準備

```python
@dataclass
class TracerParameter(BaseParameter):
    log_level: str = "INFO"
    output_dir: str = "./logs"

# param_mapに追加
param_map = {
    "device": DeviceParameter,
    "update": UpdateParameter,
    "tracer": TracerParameter,  # 新規追加
}
```

---

## 技術的特徴

- **dataclass**: 型安全でデフォルト値を持つパラメータ定義
- **dacite**: YAMLデータからdataclassインスタンスへの変換
- **ネスト対応**: パラメータ内にさらにパラメータクラスを持てる
- **YAML連携**: 設定ファイルとの双方向変換

---

## 注意点

- パラメータクラスのフィールド名とYAMLキーは一致させる必要がある
- ネストしたパラメータの場合、適切なデフォルト値設定が重要
- `dacite.from_dict()`を使用するため、型変換の制約に注意
