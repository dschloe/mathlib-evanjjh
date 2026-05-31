# mathlib-evanjjh

> A class-based Python utility package for arithmetic, geometric sequences, and trigonometry  
> **uv** 기반 프로젝트 관리

---

## 환경 정보

| 항목 | 값 |
|---|---|
| GitHub username | `dschloe` |
| PyPI username | `evanjjh` |
| GitHub repo URL | `https://github.com/dschloe/mathlib-evanjjh` |
| PyPI 패키지명 | `mathlib-evanjjh` |

---

## 프로젝트 구조

```
mathlib-evanjjh/
├── .pypirc              # ⚠️ 홈 디렉토리(~/)에 위치 — git에 올라가지 않음
├── pyproject.toml
├── README.md
├── LICENSE
├── src/
│   └── mathlib_evanjjh/
│       ├── __init__.py
│       ├── arithmetic.py      # v0.1.0
│       ├── geometric.py       # v0.2.0
│       └── trigonometry.py    # v0.3.0
└── tests/
    ├── __init__.py
    ├── test_arithmetic.py
    ├── test_geometric.py
    └── test_trigonometry.py
```

---

## 프로젝트 초기 세팅 (최초 1회)

### Step 0-1. PyPI API 토큰 저장 (최초 1회)

```bash
# 홈 디렉토리에 .pypirc 파일 생성
nano ~/.pypirc
```

아래 내용 붙여넣기:

```ini
[pypi]
username = __token__
password = pypi-AgEIcHlwaS5vcmcCJDMyNGNkN2NlLTJhOWQtNGQwMS05ZGFkLTQ1NzdkN2JiYjk2YQACKlszLCI1
```

저장: `Ctrl+X` → `Y` → `Enter`

```bash
# 저장 확인
cat ~/.pypirc
```

---

### Step 0-2. 프로젝트 초기화

```bash
# clone 된 폴더로 이동
cd mathlib-evanjjh

# uv 초기화
uv init .

# src 레이아웃 패키지 폴더 생성
mkdir -p src/mathlib_evanjjh
touch src/mathlib_evanjjh/__init__.py

# tests 폴더 생성
mkdir tests
touch tests/__init__.py

# pytest 개발 의존성 추가
uv add --dev pytest
```

---

### Step 0-3. `pyproject.toml` 설정

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "mathlib-evanjjh"
version = "0.1.0"
authors = [{ name = "Evan JJH", email = "evan@example.com" }]
description = "A class-based Python utility package for arithmetic, geometric sequences, and trigonometry"
readme = "README.md"
requires-python = ">=3.8"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.urls]
Homepage = "https://github.com/dschloe/mathlib-evanjjh"

[dependency-groups]
dev = ["pytest>=8.0"]
```

---

### Step 0-4. `.gitignore` 확인

`.gitignore` 파일에 아래 항목이 있는지 확인 (없으면 추가):

```
dist/
*.egg-info/
__pycache__/
.venv/
```

> ⚠️ `.pypirc` 는 홈 디렉토리(`~/`)에 있으므로 git과 무관합니다.  
> 절대 프로젝트 폴더 안에 두지 마세요!

---

# Step 1 — v0.1.0 : Arithmetic 클래스 (사칙연산)

## 1-1. 코드 작성

`src/mathlib_evanjjh/arithmetic.py` 생성:

```python
class Arithmetic:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            raise ValueError("0으로 나눌 수 없습니다.")
        return self.a / self.b
```

## 1-2. 테스트 작성

`tests/test_arithmetic.py` 생성:

```python
import pytest
from mathlib_evanjjh.arithmetic import Arithmetic

class TestArithmetic:
    def test_add(self):
        assert Arithmetic(3, 2).add() == 5

    def test_subtract(self):
        assert Arithmetic(10, 4).subtract() == 6

    def test_multiply(self):
        assert Arithmetic(3, 7).multiply() == 21

    def test_divide(self):
        assert Arithmetic(10, 2).divide() == 5.0

    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            Arithmetic(5, 0).divide()
```

## 1-3. 테스트 실행

```bash
uv run pytest tests/test_arithmetic.py -v
```

### 예상 결과

```
tests/test_arithmetic.py::TestArithmetic::test_add            PASSED
tests/test_arithmetic.py::TestArithmetic::test_subtract       PASSED
tests/test_arithmetic.py::TestArithmetic::test_multiply       PASSED
tests/test_arithmetic.py::TestArithmetic::test_divide         PASSED
tests/test_arithmetic.py::TestArithmetic::test_divide_by_zero PASSED
5 passed in 0.01s
```

## 1-4. 빌드 & 배포

```bash
uv build
uv publish    # ~/.pypirc 에 토큰 저장되어 있으므로 자동 인증
```

## 1-5. git push

```bash
git add .
git commit -m "v0.1.0: Arithmetic 클래스 추가"
git push origin main
```

## 1-6. 설치 확인

```bash
uv pip install mathlib-evanjjh==0.1.0
```

```python
from mathlib_evanjjh.arithmetic import Arithmetic

calc = Arithmetic(10, 2)
print(calc.add())       # 12
print(calc.subtract())  # 8
print(calc.multiply())  # 20
print(calc.divide())    # 5.0
```

---

# Step 2 — v0.2.0 : GeometricSequence 클래스 (등비수열) 추가

## 2-1. 코드 작성

`src/mathlib_evanjjh/geometric.py` 생성:

```python
class GeometricSequence:
    def __init__(self, first, ratio, n):
        self.first = first
        self.ratio = ratio
        self.n = n

    def generate(self):
        """Return a list of n terms of the geometric sequence."""
        return [self.first * (self.ratio ** i) for i in range(self.n)]

    def nth_term(self, k):
        """Return the k-th term (1-indexed)."""
        return self.first * (self.ratio ** (k - 1))

    def sum(self):
        """Return the sum of the geometric sequence."""
        if self.ratio == 1:
            return self.first * self.n
        return self.first * (1 - self.ratio ** self.n) / (1 - self.ratio)
```

## 2-2. 테스트 작성

`tests/test_geometric.py` 생성:

```python
from mathlib_evanjjh.geometric import GeometricSequence

class TestGeometricSequence:
    def test_generate(self):
        assert GeometricSequence(1, 2, 5).generate() == [1, 2, 4, 8, 16]

    def test_nth_term(self):
        assert GeometricSequence(1, 2, 5).nth_term(3) == 4

    def test_sum(self):
        assert GeometricSequence(1, 2, 5).sum() == 31.0

    def test_ratio_one(self):
        assert GeometricSequence(5, 1, 3).generate() == [5, 5, 5]

    def test_empty(self):
        assert GeometricSequence(1, 2, 0).generate() == []
```

## 2-3. 테스트 실행

```bash
uv run pytest tests/test_geometric.py -v
```

### 예상 결과

```
tests/test_geometric.py::TestGeometricSequence::test_generate  PASSED
tests/test_geometric.py::TestGeometricSequence::test_nth_term  PASSED
tests/test_geometric.py::TestGeometricSequence::test_sum       PASSED
tests/test_geometric.py::TestGeometricSequence::test_ratio_one PASSED
tests/test_geometric.py::TestGeometricSequence::test_empty     PASSED
5 passed in 0.01s
```

## 2-4. 버전 수정 & 빌드 & 배포

`pyproject.toml` 에서 버전 수정:
```toml
version = "0.2.0"
```

```bash
uv build
uv publish
```

## 2-5. git push

```bash
git add .
git commit -m "v0.2.0: GeometricSequence 클래스 추가"
git push origin main
```

## 2-6. 설치 확인

```bash
uv pip install --upgrade mathlib-evanjjh
```

```python
from mathlib_evanjjh.geometric import GeometricSequence

gs = GeometricSequence(first=1, ratio=2, n=5)
print(gs.generate())    # [1, 2, 4, 8, 16]
print(gs.nth_term(3))   # 4
print(gs.sum())         # 31.0
```

---

# Step 3 — v0.3.0 : Trigonometry 클래스 (삼각함수) 추가

## 3-1. 코드 작성

`src/mathlib_evanjjh/trigonometry.py` 생성:

```python
import math

class Trigonometry:
    def __init__(self, angle_deg):
        self.angle_deg = angle_deg
        self._rad = math.radians(angle_deg)

    def sin(self):
        return round(math.sin(self._rad), 10)

    def cos(self):
        return round(math.cos(self._rad), 10)

    def tan(self):
        if self.angle_deg % 180 == 90:
            raise ValueError("tan(90°) is undefined.")
        return round(math.tan(self._rad), 10)
```

## 3-2. 테스트 작성

`tests/test_trigonometry.py` 생성:

```python
import pytest
from mathlib_evanjjh.trigonometry import Trigonometry

class TestTrigonometry:
    def test_sin(self):
        assert Trigonometry(30).sin() == pytest.approx(0.5)

    def test_cos(self):
        assert Trigonometry(60).cos() == pytest.approx(0.5)

    def test_tan(self):
        assert Trigonometry(45).tan() == pytest.approx(1.0)

    def test_tan_undefined(self):
        with pytest.raises(ValueError):
            Trigonometry(90).tan()
```

## 3-3. 테스트 실행

```bash
uv run pytest tests/test_trigonometry.py -v
```

### 예상 결과

```
tests/test_trigonometry.py::TestTrigonometry::test_sin           PASSED
tests/test_trigonometry.py::TestTrigonometry::test_cos           PASSED
tests/test_trigonometry.py::TestTrigonometry::test_tan           PASSED
tests/test_trigonometry.py::TestTrigonometry::test_tan_undefined PASSED
4 passed in 0.01s
```

## 3-4. 버전 수정 & 빌드 & 배포

`pyproject.toml` 에서 버전 수정:
```toml
version = "0.3.0"
```

```bash
uv build
uv publish
```

## 3-5. git push

```bash
git add .
git commit -m "v0.3.0: Trigonometry 클래스 추가"
git push origin main
```

## 3-6. 설치 확인

```bash
uv pip install --upgrade mathlib-evanjjh
```

```python
from mathlib_evanjjh.trigonometry import Trigonometry

print(Trigonometry(30).sin())   # 0.5
print(Trigonometry(60).cos())   # 0.5
print(Trigonometry(45).tan())   # 1.0
```

---

## 전체 테스트 한번에 실행

```bash
uv run pytest tests/ -v
```

### 최종 결과

```
tests/test_arithmetic.py::TestArithmetic::test_add               PASSED
tests/test_arithmetic.py::TestArithmetic::test_subtract          PASSED
tests/test_arithmetic.py::TestArithmetic::test_multiply          PASSED
tests/test_arithmetic.py::TestArithmetic::test_divide            PASSED
tests/test_arithmetic.py::TestArithmetic::test_divide_by_zero    PASSED
tests/test_geometric.py::TestGeometricSequence::test_generate    PASSED
tests/test_geometric.py::TestGeometricSequence::test_nth_term    PASSED
tests/test_geometric.py::TestGeometricSequence::test_sum         PASSED
tests/test_geometric.py::TestGeometricSequence::test_ratio_one   PASSED
tests/test_geometric.py::TestGeometricSequence::test_empty       PASSED
tests/test_trigonometry.py::TestTrigonometry::test_sin           PASSED
tests/test_trigonometry.py::TestTrigonometry::test_cos           PASSED
tests/test_trigonometry.py::TestTrigonometry::test_tan           PASSED
tests/test_trigonometry.py::TestTrigonometry::test_tan_undefined PASSED
14 passed in 0.03s
```

---

## 버전별 작업 흐름 요약

```
[최초 1회]  nano ~/.pypirc → 토큰 저장
            uv init . → 폴더 생성 → pyproject.toml 설정

[v0.1.0]   코드 작성 → 테스트 → uv build → uv publish → git push
[v0.2.0]   코드 추가 → 테스트 → version 수정 → uv build → uv publish → git push
[v0.3.0]   코드 추가 → 테스트 → version 수정 → uv build → uv publish → git push
```

---

## 버전 히스토리

| 버전 | 추가 클래스 | 메서드 |
|------|------------|--------|
| 0.1.0 | `Arithmetic(a, b)` | `add()` `subtract()` `multiply()` `divide()` |
| 0.2.0 | `GeometricSequence(first, ratio, n)` | `generate()` `nth_term(k)` `sum()` |
| 0.3.0 | `Trigonometry(angle_deg)` | `sin()` `cos()` `tan()` |

---

## 라이선스

MIT License
