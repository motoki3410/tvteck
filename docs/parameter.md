# パラメータ管理の仕組み

## 概要

TVTeckプロジェクトでは、テストや各種処理で利用する設定値（パラメータ）を一元管理するために `ParameterManager` クラスを用意しています。
パラメータはカテゴリごと（例: device, update）にクラスとして定義され、柔軟かつ拡張性の高い設計となっています。

---

## 主な構成

### ParameterManager

- パラメータカテゴリとクラスのマッピング（`param_map`）を保持
- 各カテゴリのパラメータインスタンスを `self.parameters` で管理

#### 主なメソッド

| メソッド名 | 役割 |
|------------|------|
| `set_parameter(name, param)` | 指定カテゴリにパラメータインスタンスをセット |
| `set_all_parameters()` | 全カテゴリのパラメータをデフォルトで初期化 |
| `get_field_names(category)` | 指定カテゴリのフィールド名一覧を取得 |
| `get_all_category_field_names()` | 全カテゴリのフィールド名一覧を取得 |
| `dump_parameter(category)` | 指定カテゴリのパラメータ内容を表示 |

---

### パラメータクラス

- 例: `DeviceParameter`, `UpdateParameter`
- 各カテゴリごとに dataclass などで定義
- フィールド名や値を管理し、`get_field_names()` や `dump_parameter()` などのメソッドを持つ

---

## 拡張方法

- 新しいパラメータカテゴリを追加する場合は、対応するクラスを作成し、`param_map` に追加するだけで管理対象にできます。

---

## 利用例

```python
pm = ParameterManager()
pm.set_all_parameters()
print(pm.get_field_names("device"))
pm.dump_parameter("update")
```

---

## 注意点

- パラメータクラスのファイル名や import パスの一貫性に注意してください。
- パラメータ値の初期化や外部設定ファイルとの連携は今後の拡張余地があります。
