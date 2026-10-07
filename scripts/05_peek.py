import importlib.util, pathlib, inspect
_spec = importlib.util.spec_from_file_location('reg', pathlib.Path(__file__).with_name('03_registered.py')); reg = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(reg)
print(inspect.getsource(reg.fit)); print(inspect.getsource(reg.build_formula)[:2500])
