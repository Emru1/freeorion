from typing import Any, TypeVar

from typing_extensions import Self

class _PlanetType: ...

Swamp = _PlanetType()
Toxic = _PlanetType()
Inferno = _PlanetType()
Radiated = _PlanetType()
Barren = _PlanetType()
Tundra = _PlanetType()
Desert = _PlanetType()
Terran = _PlanetType()
Ocean = _PlanetType()
AsteroidsType = _PlanetType()
GasGiantType = _PlanetType()

class _PlanetEnvironment: ...

Good = _PlanetEnvironment()
Adequate = _PlanetEnvironment()
Poor = _PlanetEnvironment()
Hostile = _PlanetEnvironment()
Uninhabitable = _PlanetEnvironment()

class _PlanetSize: ...

class FloatValue:
    def __add__(self, other: FloatValue | float) -> FloatValue: ...
    def __radd__(self, other: FloatValue | float) -> FloatValue: ...
    def __sub__(self, other: FloatValue | float) -> FloatValue: ...
    def __rsub__(self, other: FloatValue | float) -> FloatValue: ...
    def __mul__(self, other: FloatValue | float) -> FloatValue: ...
    def __rmul__(self, other: FloatValue | float) -> FloatValue: ...
    def __floordiv__(self, other) -> FloatValue: ...
    def __rfloordiv__(self, other: FloatValue | float) -> FloatValue: ...
    def __truediv__(self, other) -> FloatValue: ...
    def __rtruediv__(self, other: FloatValue | float) -> FloatValue: ...
    def __pow__(self, other: FloatValue | float) -> FloatValue: ...
    def __rpow__(self, other: FloatValue | float) -> FloatValue: ...

ComparableType = TypeVar("ComparableType", type[str], type[float])

class Target:
    Owner = ...
    Population = FloatValue()
    TargetPopulation = FloatValue()
    MaxSupply = FloatValue()
    Happiness = FloatValue()
    MaxTroops = FloatValue()

class _Empire: ...

AnyEmpire = _Empire()

class Source:
    """
    FOCS Source is IsSource, this class is fpr Source.<something>
    """

    Owner: _Empire
    ID: Any
    SystemID: Any

class _Scope:
    def __and__(self, other) -> _Scope: ...
    def __or__(self, other) -> _Scope: ...
    def __invert__(self) -> _Scope: ...

class _Turn(_Scope):
    def __lt__(self, other) -> _Turn: ...

CurrentTurn = _Turn()

class LocalCandidate:
    LastTurnConquered = _Turn()
    LastTurnAttackedByShip = _Turn()

def Planet(
    *, type: list[_PlanetType] = [], environment: list[_PlanetEnvironment] = [], size: list[_PlanetSize] = []
) -> _Scope: ...
def HasSpecies() -> _Scope: ...
def Homeworld() -> _Scope: ...

System = _Scope()
Ship = _Scope()
Armed = _Scope()
Unowned = _Scope()
Capital = _Scope()
IsHuman = _Scope()

class _IntComparableScope(_Scope):
    def __eq__(self, other) -> _Scope: ...  # type: ignore[override]

GalaxyMaxAIAggression = _IntComparableScope()

def TargetIndustry(*, low: int) -> _Scope: ...
def Happiness(*, low: int) -> _Scope: ...
def Focus(*, type: list[str]) -> _Scope: ...

class FocusTypeObject: ...

def FocusType(
    *,
    name: str,
    description: str,
    location=_Scope,
    graphic=str,
) -> FocusTypeObject: ...
def OwnedBy(*, affiliation: _Empire = _Empire(), empire: _Empire = _Empire()) -> _Scope: ...
def WithinStarlaneJumps(*, jumps: int, condition: _Scope) -> _Scope: ...
def Contains(scope=_Scope) -> _Scope: ...
def Turn(high: int = 0, low: int = 0) -> _Scope: ...
def DesignHasPart(*, name: str) -> _Scope: ...

class _Resource: ...

Influence = _Resource()

def HasEmpireStockpile(empire: _Empire, resource: _Resource, low: int) -> _Scope: ...

class _Effect: ...

T = TypeVar("T")

class ValuePlaceHolder(FloatValue):
    def __call__(self, T):
        return Self

Value = ValuePlaceHolder()

def Abs(type_: ComparableType, value: T) -> FloatValue: ...
def MinOf(type_: ComparableType, *args: T) -> FloatValue: ...
def MaxOf(type_: ComparableType, *args: T) -> FloatValue: ...
def StatisticIf(type_: ComparableType, condition: _Scope) -> FloatValue: ...
def StatisticCount(type_: ComparableType, condition: _Scope) -> FloatValue: ...
def NamedReal(*, name: str, value: FloatValue | float) -> FloatValue: ...
def NamedRealLookup(*, name: str) -> FloatValue | float: ...
def EmpireStockpile(empire: _Empire, resource: _Resource) -> FloatValue: ...
def PartCapacity(*, name: str) -> FloatValue: ...
def SetMaxShield(*, value: FloatValue | float) -> _Effect: ...
def SetTargetIndustry(*, value: FloatValue | float) -> _Effect: ...
def SetMaxTroops(*, value: FloatValue | float) -> _Effect: ...
def SetTargetHappiness(*, value: FloatValue | float) -> _Effect: ...
def SetPopulation(*, value: FloatValue | float) -> _Effect: ...
def SetTroops(*, value: FloatValue | float) -> _Effect: ...
def SetMaxDefense(*, value: FloatValue | float) -> _Effect: ...
def SetSupply(*, value: FloatValue | float) -> _Effect: ...
def SetTargetResearch(*, value: FloatValue | float) -> _Effect: ...
def SetMaxSupply(*, value: FloatValue | float) -> _Effect: ...
def SetTargetPopulation(*, value: FloatValue | float) -> _Effect: ...
def SetTargetInfluence(*, value: FloatValue | float) -> _Effect: ...
def SetRebelTroops(*, value: FloatValue | float) -> _Effect: ...
def CreateBuilding(*, type: str) -> _Effect: ...
def CreateShip(*, designname: str, species: str) -> _Effect: ...
def SetCapacity(*, partname: str, value: float | FloatValue) -> _Effect: ...
def SetMaxDamage(*, partname: str, value: FloatValue) -> _Effect: ...
def SetMaxSecondaryStat(*, partname: str, value: FloatValue) -> _Scope: ...

class _StarType: ...

Blue = _StarType()

def SetStarType(*, type: _StarType) -> _Effect: ...
def GenerateSitRepMessage(
    message: str,
    label: str,
    icon: str,
    parameters: dict[str, Any],
    empire: _Empire,
) -> _Effect: ...
def GiveEmpireTech(name: str, empire) -> _Effect: ...
def EffectsGroup(
    *,
    scope: _Scope,
    effects: list[_Effect] | _Effect,
    activation: _Scope = _Scope(),
    description: str = "",
    priority=None,
    accountinglabel: str = "",
    stackinggroup: str = "",
): ...

IsSource = _Scope()

def Object(id) -> _Scope: ...