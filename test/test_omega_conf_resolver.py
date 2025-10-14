from pytest import fixture, mark

from omegaconf import OmegaConf
import omegaconf_resolver

omegaconf_resolver.register()

def test_length():
    cfg = OmegaConf.create({
        "test_list": [1, 2, 3],
        "len_ref": "${length:${test_list}}",
        "len": "${length:[1, 2, 3, 4, 5]}"
    })
    
    assert cfg["len_ref"] == 3
    assert cfg["len"] == 5

def test_array():
    import numpy as np
    cfg = OmegaConf.create({
        "test_list": [1, 2, 3],
        "arr_ref": "${array:${test_list}}",
        "arr": "${array:[1, 2, 3, 4, 5]}"
    })
    
    assert (cfg["arr_ref"] == np.asarray([1, 2, 3])).all()
    assert (cfg["arr"] == np.asarray([1, 2, 3, 4, 5])).all()
    
def test_mult():
    cfg = OmegaConf.create({
        "a": 3,
        "b": 2,
        "mult_ref": "${mult:${a},${b}}",
        "mult": "${mult:3,2}"
    })
    
    assert cfg["mult_ref"] == 6
    assert cfg["mult"] == 6
    
def test_div():
    cfg = OmegaConf.create({
        "a": 3,
        "b": 2,
        "div_ref": "${div:${a},${b}}",
        "div": "${div:3,2}"
    })
    
    assert cfg["div_ref"] == 1.5
    assert cfg["div"] == 1.5
    
def test_intdiv():
    cfg = OmegaConf.create({
        "a": 3,
        "b": 2,
        "intdiv_ref": "${intdiv:${a},${b}}",
        "intdiv": "${intdiv:3,2}"
    })
    
    assert cfg["intdiv_ref"] == 1
    assert cfg["intdiv"] == 1
    
def test_if_cond():
    cfg = OmegaConf.create({
        "cond": True,
        "if_cond_ref": "${if_cond:${cond},'yes','no'}",
        "if_cond": "${if_cond:true,'yes','no'}"
    })
    
    assert cfg["if_cond_ref"] == "yes"
    assert cfg["if_cond"] == "yes"
    
    cfg = OmegaConf.create({
        "cond": False,
        "if_cond_ref": "${if_cond:${cond},'yes','no'}",
        "if_cond": "${if_cond:false,'yes','no'}"
    })

    assert cfg["if_cond_ref"] == "no"
    assert cfg["if_cond"] == "no"
    
def test_add():
    cfg = OmegaConf.create({
        "a": 3,
        "b": 2,
        "add_ref": "${add:${a},${b}}",
        "add": "${add:3,2}"
    })
    
    assert cfg["add_ref"] == 5
    assert cfg["add"] == 5
    
    
def test_sub():
    cfg = OmegaConf.create({
        "a": 3,
        "b": 2,
        "sub_ref": "${sub:${a},${b}}",
        "sub": "${sub:3,2}"
    })
    
    assert cfg["sub_ref"] == 1
    assert cfg["sub"] == 1
    
def test_path_join():
    cfg = OmegaConf.create({
        "base_path": "/home/user/test_base_path",
        "subdir1": "subdir1",
        "subdir2": "subdir2",
        "path_join_ref": "${path_join:${base_path},${subdir1},${subdir2}}",
        "path_join": "${path_join:/home/user/test_base_path,subdir1,subdir2}"
    })
    
    assert cfg["path_join_ref"] == "/home/user/test_base_path/subdir1/subdir2"
    assert cfg["path_join"] == "/home/user/test_base_path/subdir1/subdir2"

def test_resolver():
    test_length()
    test_array()
    test_mult()
    test_div()
    test_intdiv()
    test_if_cond()
    test_add()
    test_sub()
    test_path_join()

def test_resolver_with_hydra():
    import hydra
    
    hydra.initialize(config_path="../examples/config")
    cfg = hydra.compose(config_name="config")
    cfg = OmegaConf.to_object(cfg)
    
    assert cfg["len_ref"] == 3
    assert cfg["len"] == 5

    import numpy as np
    assert (cfg["arr_ref"] == np.asarray([1, 2, 3])).all()
    assert (cfg["arr"] == np.asarray([1, 2, 3, 4, 5])).all()

    assert cfg["mult_ref"] == 6
    assert cfg["mult"] == 6
    
    assert cfg["div_ref"] == 1.5
    assert cfg["div"] == 1.5
    
    assert cfg["intdiv_ref"] == 1
    assert cfg["intdiv"] == 1
    
    assert cfg["if_cond_ref"] == "yes"
    assert cfg["if_cond"] == "yes"
    
    assert cfg["add_ref"] == 5
    assert cfg["add"] == 5
    
    assert cfg["sub_ref"] == 1
    assert cfg["sub"] == 1
    
    assert cfg["path_join_ref"] == "/home/user/test_base_path/subdir1/subdir2"
    assert cfg["path_join"] == "/home/user/test_base_path/subdir1/subdir2"