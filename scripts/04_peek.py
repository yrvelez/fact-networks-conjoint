import importlib.util, pathlib, inspect
_spec = importlib.util.spec_from_file_location('reg', pathlib.Path(__file__).with_name('03_registered.py')); reg = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(reg)
print(inspect.getsource(reg.build_formula)); print(inspect.getsource(reg.fit))
H = reg.HYPOTHESES
h = H[0] if isinstance(H, list) else list(H.values())[0]
print({k: v for k, v in h.items()})
