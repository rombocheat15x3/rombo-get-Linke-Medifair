import requests, random, string, re, json, time, hashlib, base64, threading, asyncio, aiohttp, ssl, urllib.parse
from datetime import datetime
from typing import Optional, Dict, Any, List
from dataclasses import dataclass, field
from enum import Enum, auto

@dataclass(frozen=True)
class _K:
    V: str = "0.1"
    O: str = "الذئب الأبيض"
    T: str = "@j49_c"
    C1: str = "@bshshshkk"
    C2: str = "@BQBOOB"
    _U: str = field(default="aHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdA==", repr=False)
    
    @property
    def B(self) -> str:
        return base64.b64decode(self._U).decode()

class _S(Enum):
    IDLE = auto()
    PROC = auto()
    SUCC = auto()
    FAIL = auto()

@dataclass
class _R:
    s: _S = _S.IDLE
    d: Any = None
    e: Optional[str] = None
    t: float = field(default_factory=time.time)

class _L:
    _i = None
    def new(cls):
        if cls._i is None:
            cls._i = super().new(cls)
            cls._i._h = []
        return cls._i
    
    def log(self, m: str, t: str = "INFO"):
        ts = datetime.now().strftime("%H:%M:%S")
        self._h.append(f"[{ts}] {t}: {m}")
    
    def get(self) -> List[str]:
        return self._h[-10:]

class _P:
    def init(self):
        self._cache: Dict[str, Any] = {}
        self._pat = re.compile(r'^(https?://)?(www\.)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(/.*)?$')
    
    def _v(self, u: str) -> bool:
        return bool(self._pat.match(u))
    
    def _g(self, u: str) -> str:
        pool = string.ascii_letters + string.digits
        return ''.join(random.choices(pool, k=8)) + hashlib.md5(u.encode()).hexdigest()[:6]
    
    async def exec(self, ctx: Dict[str, Any]) -> _R:
        url = ctx.get('url', '')
        if not self._v(url):
            return _R(s=_S.FAIL, e="الرابط ميّت.. جرب رابط حيّ")
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        ctx['url'] = url
        ctx['sig'] = self._g(url)
        return _R(s=_S.SUCC, d=ctx)

class _X:
    def init(self):
        self._ep = "http://tinyurl.com/api-create.php"
    
    async def exec(self, ctx: Dict[str, Any]) -> _R:
        url = ctx.get('url')
        sig = ctx.get('sig')
        
        _L().log(f"بدء تشويه الرابط {sig[:8]}..")
        
        try:
            async with aiohttp.ClientSession() as s:
                async with s.get(f"{self._ep}?url={urllib.parse.quote(url)}", 
                               timeout=aiohttp.ClientTimeout(total=10),
                               ssl=ssl.create_default_context()) as r:
                    if r.status == 200:
                        txt = await r.text()
                        if txt and not txt.startswith('Error'):
                            return _R(s=_S.SUCC, d={**ctx, 'short': txt})
                    return _R(s=_S.FAIL, e="الخدمة نايمة.. جرب بعدين")
        except Exception as ex:
            return _R(s=_S.FAIL, e=f"شي طاح بالبحر: {str(ex)[:30]}")

class _A:
    async def exec(self, ctx: Dict[str, Any]) -> _R:
        short = ctx.get('short', 'مافيه')
        orig = ctx.get('url', 'مجهول')
        
        art = [
            "تمّ التصغير بنجاح.. والرابط الجديد خفيف كالشبح",
            "اختصرته لك.. والحين يقدر يمشي بسرعة الريح",
            "الرابط طويل كان يزعج.. والحين قصير وناعم",
            "صغّرته بسحر الذئب.. وصار جاهز للاستخدام"
        ]
        
        msg = f"""{random.choice(art)}

🔗 الرابط المختصر: {short}
🔒 الأصلي المقفول: {orig[:50]}{'..' if len(orig) > 50 else ''}

📌 الإصدار: {_K().V}
👤 {_K().O} | {_K().T}
📢 {_K().C1} | {_K().C2}"""
        
        return _R(s=_S.SUCC, d=msg)

class _B:
    def init(self, t: str):
        self.k = _K()
        self.t = t
        self.u = f"{self.k.B}{t}"
        self.o = 0
        self._pool: Dict[int, _S] = {}
