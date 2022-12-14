from utils.callbacks import *
import os

def build_config(filename):
    folder = os.path.split(filename)[0]
    POSCAR = os.path.join(folder, 'POSCAR')
    return {
    "zh-name": "第一性原理数据",
    "tag_name": "firstprinciples_data",
    "type": "container",
    "children": [
        {
            "zh-name": "管理信息",
            "tag_name": "management_information",
            "type": "container",
            "children": [
                {
                    "zh-name": "计算软件",
                    "tag_name": "Calculation_Software",
                    "type": "uncheck-stringtype",
                    "default": "VASP",
                    "path": "",
                    "xpath": "",
                    "callback": "",
                    "kwargs": {}
                },
                {
                    "zh-name": "软件版本",
                    "tag_name": "Software_version",
                    "type": "uncheck-stringtype",
                    "default": "",
                    "path": filename,
                    "xpath": ".//generator/i[@name='version']",
                    "callback": '',
                    "kwargs": {}
                },
                {
                    "zh-name": "计算内容",
                    "tag_name": "Calculate_content",
                    "type": "uncheck-stringtype",
                    "default": "",
                    "path": "",
                    "xpath": "",
                    "callback": "",
                    "kwargs": {}
                },
                {
                    "zh-name": "计算时间",
                    "tag_name": "calculating_time",
                    "type": "uncheck-stringtype",
                    "default": "",
                    "path": filename,
                    "xpath": ".//generator/i[@name='date']",
                    "callback": '',
                    "kwargs": {}
                },
                {
                    "zh-name": "计算人员",
                    "tag_name": "computing_staff",
                    "type": "uncheck-stringtype",
                    "default": "",
                    "path": "",
                    "xpath": "",
                    "callback": "",
                    "kwargs": {}
                },
                {
                    "zh-name": "关键字",
                    "tag_name": "keyword",
                    "type": "uncheck-stringtype",
                    "default": "",
                    "path": "",
                    "xpath": "",
                    "callback": "",
                    "kwargs": {}
                }
            ]
        },
        {
            "zh-name": "输入",
            "tag_name": "enter",
            "type": "container",
            "children": [
                {
                    "zh-name": "计算参数",
                    "tag_name": "Calculated_parameters",
                    "type": "container",
                    "children": [
                        {
                            "zh-name": "计算类型",
                            "tag_name": "calculation_type",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "力收敛半径",
                            "tag_name": "force_convergence_radius",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "能量收敛半径",
                            "tag_name": "energy_convergence_radius",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "迭代步数",
                            "tag_name": "Iteration_steps",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": filename,
                            "xpath": ".//separator/i[@name='NSW']",
                            "callback": "",
                            "kwargs": {}
                        }
                    ]
                },
                {
                    "zh-name": "系统参数",
                    "tag_name": "System_parameters",
                    "type": "container",
                    "children": [
                        {
                            "zh-name": "布拉维格子",
                            "tag_name": "Bravais_lattice",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "原子个数",
                            "tag_name": "number_of_atoms",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": filename,
                            "xpath": ".//atominfo/atoms",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "原子种类数",
                            "tag_name": "number_of_atomic_species",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": filename,
                            "xpath": ".//atominfo/types",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "体系电荷数",
                            "tag_name": "system_charge",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "外加电荷",
                            "tag_name": "applied_charge",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "截断能",
                            "tag_name": "cutoff_energy",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": filename,
                            "xpath": ".//incar/i[@name='ENCUT']",
                            "callback": lambda l: l[0].text + 'eV' if l else '',
                            "kwargs": {}
                        },
                        {
                            "zh-name": "高斯扩展值",
                            "tag_name": "Gaussian_spread_value",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "离散方法",
                            "tag_name": "discrete_method",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "交换关联泛函",
                            "tag_name": "exchangecorrelation_functional",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "库伦相互作用",
                            "tag_name": "Coulomb_interaction",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "库伦嵌入截断",
                            "tag_name": "Coulomb_embedding_truncation",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        }
                    ]
                },
                {
                    "zh-name": "电子参数",
                    "tag_name": "Electronic_parameters",
                    "type": "container",
                    "children": [
                        {
                            "zh-name": "电子迭代最大步数",
                            "tag_name": "Electronic_iteration_maximum_number_of_steps",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": filename,
                            "xpath": ".//incar/NELM",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "收敛半径",
                            "tag_name": "radius_of_convergence",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "自洽混合参数",
                            "tag_name": "Selfconsistent_mixing_parameters",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "自洽混合模型",
                            "tag_name": "selfconsistent_mixed_model",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "电子最小化",
                            "tag_name": "Electron_minimization",
                            "type": "container",
                            "children": [
                                {
                                    "zh-name": "迭代次数",
                                    "tag_name": "number_of_iterations",
                                    "type": "uncheck-stringtype",
                                    "default": "",
                                    "path": "",
                                    "xpath": "",
                                    "callback": "",
                                    "kwargs": {}
                                },
                                {
                                    "zh-name": "截断标准",
                                    "tag_name": "truncation_criterion",
                                    "type": "uncheck-stringtype",
                                    "default": "",
                                    "path": "",
                                    "xpath": "",
                                    "callback": "",
                                    "kwargs": {}
                                }
                            ]
                        },
                        {
                            "zh-name": "电子优化",
                            "tag_name": "Electronic_optimization",
                            "type": "container",
                            "children": [
                                {
                                    "zh-name": "迭代次数",
                                    "tag_name": "number_of_iterations",
                                    "type": "uncheck-stringtype",
                                    "default": "",
                                    "path": "",
                                    "xpath": "",
                                    "callback": "",
                                    "kwargs": {}
                                },
                                {
                                    "zh-name": "截断标准",
                                    "tag_name": "truncation_criterion",
                                    "type": "uncheck-stringtype",
                                    "default": "",
                                    "path": filename,
                                    "xpath": ".//incar/i[@name='ENCUT']",
                                    "callback": "",
                                    "kwargs": {}
                                }
                            ]
                        }
                    ]
                },
                {
                    "zh-name": "离子参数",
                    "tag_name": "Ion_parameters",
                    "type": "container",
                    "children": [
                        {
                            "zh-name": "离子动力学方法",
                            "tag_name": "ion_kinetic_method",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        }
                    ]
                },
                {
                    "zh-name": "晶胞参数",
                    "tag_name": "Cell_parameters",
                    "type": "container",
                    "children": [
                        {
                            "zh-name": "晶胞动力学方法",
                            "tag_name": "Unit_Cell_Dynamics_Method",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "晶胞压力",
                            "tag_name": "unit_cell_pressure",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "压力收敛半径",
                            "tag_name": "pressure_convergence_radius",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "晶胞固定参数",
                            "tag_name": "Cell_Fixed_Parameters",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "晶格参数",
                            "tag_name": "Lattice_parameters",
                            "type": "table",
                            "default": "",
                            "path": POSCAR,
                            "xpath": "",
                            "regex": "",
                            "callback": lattice_parameters_callback,
                            "kwargs": {
                                "columns": [
                                    "x",
                                    "y",
                                    "z"
                                ],
                                "units": [
                                    "",
                                    "",
                                    ""
                                ]
                            }
                        }
                    ]
                },
                {
                    "zh-name": "原子参数",
                    "tag_name": "Atomic_parameters",
                    "type": "container",
                    "children": [
                        {
                            "zh-name": "原子种类",
                            "tag_name": "Atomic_species",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": filename,
                            "xpath": ".//array[@name='atomtypes']/set/rc",
                            "callback": lambda l: ', '.join(list(set([rc[1].text for rc in l]))),
                            "kwargs": {}
                        },
                        {
                            "zh-name": "相对原子质量",
                            "tag_name": "relative_atomic_mass",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": filename,
                            "xpath": ".//array[@name='atomtypes']/set/rc",
                            "callback": lambda l: ', '.join(list(set([rc[2].text for rc in l]))),
                            "kwargs": {}
                        },
                        {
                            "zh-name": "原子赝势",
                            "tag_name": "Atomic_pseudopotential",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": filename,
                            "xpath": ".//array[@name='atomtypes']/set/rc",
                            "callback": lambda l: ', '.join(list(set([rc[4].text for rc in l]))),
                            "kwargs": {}
                        },
                        {
                            "zh-name": "原子位置",
                            "tag_name": "atomic_position",
                            "type": "table",
                            "default": "",
                            "path": POSCAR,
                            "regex": "1",
                            "callback": atomic_position_callback,
                            "kwargs": {
                                "columns": [
                                    "element",
                                    "x",
                                    "y",
                                    "z"
                                ],
                                "units": [
                                    "",
                                    "",
                                    "",
                                    ""
                                ]
                            }
                        },
                        {
                            "zh-name": "K点",
                            "tag_name": "K_point",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "k点折叠",
                            "tag_name": "k_point_fold",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        }
                    ]
                },
                {
                    "zh-name": "溶液参数",
                    "tag_name": "Solution_parameters",
                    "type": "container",
                    "children": [
                        {
                            "zh-name": "溶液类型",
                            "tag_name": "Solution_type",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "溶剂",
                            "tag_name": "solvent",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "阴离子类型与浓度",
                            "tag_name": "Anion_type_and_concentration",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "阳离子类型与浓度",
                            "tag_name": "Cation_Type_and_Concentration",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "溶液最小化",
                            "tag_name": "solution_minimization",
                            "type": "container",
                            "children": [
                                {
                                    "zh-name": "迭代次数",
                                    "tag_name": "number_of_iterations",
                                    "type": "uncheck-stringtype",
                                    "default": "",
                                    "path": "",
                                    "xpath": "",
                                    "callback": "",
                                    "kwargs": {}
                                },
                                {
                                    "zh-name": "截断标准",
                                    "tag_name": "truncation_criterion",
                                    "type": "uncheck-stringtype",
                                    "default": "",
                                    "path": "",
                                    "xpath": "",
                                    "callback": "",
                                    "kwargs": {}
                                }
                            ]
                        }
                    ]
                },
                {
                    "zh-name": " 输入文件",
                    "tag_name": "input_file",
                    "type": "file-list",
                    "default": "",
                    "path": "",
                    "xpath": "",
                    "callback": "",
                    "kwargs": {
                        "filenames": [],
                        "paths": []
                    }
                }
            ]
        },
        {
            "zh-name": "输出",
            "tag_name": "output",
            "type": "container",
            "children": [
                {
                    "zh-name": "优化后晶胞参数",
                    "tag_name": "Optimized_unit_cell_parameters",
                    "type": "table",
                    "default": "",
                    "path": "",
                    "xpath": "",
                    "callback": "",
                    "kwargs": {
                        "columns": [
                            "x",
                            "y",
                            "z"
                        ],
                        "units": [
                            "",
                            "",
                            ""
                        ]
                    }
                },
                {
                    "zh-name": "优化后的原子位置",
                    "tag_name": "optimized_atomic_positions",
                    "type": "table",
                    "default": "",
                    "path": "",
                    "xpath": "",
                    "callback": "",
                    "kwargs": {
                        "columns": [
                            "element",
                            "x",
                            "y",
                            "z"
                        ],
                        "units": [
                            "",
                            "",
                            "",
                            ""
                        ]
                    }
                },
                {
                    "zh-name": "体系总体积",
                    "tag_name": "The_total_volume_of_the_system",
                    "type": "uncheck-stringtype",
                    "default": "",
                    "path": filename,
                    "xpath": ".//crystal/i[@name='volume']",
                    "callback": lambda l: l[-1].text + 'a.u.^3' if l else '',
                    "kwargs": {}
                },
                {
                    "zh-name": "体系密度",
                    "tag_name": "System_density",
                    "type": "uncheck-stringtype",
                    "default": "",
                    "path": filename,
                    "xpath": ".//dos/i[@name='efermi']",
                    "callback": lambda l: l[-1].text + 'eV' if l else '',
                    "kwargs": {}
                },
                {
                    "zh-name": "体系压力与压强",
                    "tag_name": "System_pressure_and_pressure",
                    "type": "container",
                    "children": [
                        {
                            "zh-name": "压力分布",
                            "tag_name": "force_distribution",
                            "type": "table",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {
                                "columns": [
                                    "x",
                                    "y",
                                    "z"
                                ],
                                "units": [
                                    "",
                                    "",
                                    ""
                                ]
                            }
                        },
                        {
                            "zh-name": "压强分布",
                            "tag_name": "pressure_distribution",
                            "type": "table",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {
                                "columns": [
                                    "x",
                                    "y",
                                    "z"
                                ],
                                "units": [
                                    "",
                                    "",
                                    ""
                                ]
                            }
                        }
                    ]
                },
                {
                    "zh-name": "体系总焓变",
                    "tag_name": "The_total_enthalpy_change_of_the_system",
                    "type": "uncheck-stringtype",
                    "default": "",
                    "path": "",
                    "xpath": "",
                    "callback": "",
                    "kwargs": {}
                },
                {
                    "zh-name": "费米能",
                    "tag_name": "Fermi_energy",
                    "type": "uncheck-stringtype",
                    "default": "",
                    "path": "",
                    "xpath": "",
                    "callback": "",
                    "kwargs": {}
                },
                {
                    "zh-name": "体系总能量",
                    "tag_name": "total_system_energy",
                    "type": "uncheck-stringtype",
                    "default": "",
                    "path": filename,
                    "xpath": ".//energy/i[@name='e_fr_energy']",
                    "callback": lambda l: l[-1].text + 'Ry' if l else '',
                    "kwargs": {}
                },
                {
                    "zh-name": "能量误差半径",
                    "tag_name": "Energy_error_radius",
                    "type": "uncheck-stringtype",
                    "default": "",
                    "path": "",
                    "xpath": "",
                    "callback": "",
                    "kwargs": {}
                },
                {
                    "zh-name": "收敛所使用的迭代步数",
                    "tag_name": "the_number_of_iteration_steps_used_to_converge",
                    "type": "uncheck-stringtype",
                    "default": "",
                    "path": "",
                    "xpath": "",
                    "callback": "",
                    "kwargs": {}
                },
                {
                    "zh-name": "原子受力分布",
                    "tag_name": "Atomic_Force_Distribution",
                    "type": "table",
                    "default": "",
                    "path": "",
                    "xpath": "",
                    "callback": "",
                    "kwargs": {
                        "columns": [
                            "element",
                            "force_in_the_x_direction",
                            "Force_in_the_y_direction",
                            "force_in_the_z_direction"
                        ],
                        "units": [
                            "",
                            "",
                            "",
                            ""
                        ]
                    }
                },
                {
                    "zh-name": "布局电荷分析",
                    "tag_name": "Layout_charge_analysis",
                    "type": "uncheck-stringtype",
                    "default": "",
                    "path": "",
                    "xpath": "",
                    "callback": "",
                    "kwargs": {}
                },
                {
                    "zh-name": " 输出文件",
                    "tag_name": "output_file",
                    "type": "file-list",
                    "default": "",
                    "path": "",
                    "xpath": "",
                    "callback": "",
                    "kwargs": {
                        "filenames": [],
                        "paths": []
                    }
                }
            ]
        },
        {
            "zh-name": "衍生(后处理)",
            "tag_name": "Derivation_postprocessing",
            "type": "container",
            "children": [
                {
                    "zh-name": "态密度",
                    "tag_name": "density_of_states",
                    "type": "container",
                    "children": [
                        {
                            "zh-name": "总态密度",
                            "tag_name": "total_density_of_states",
                            "type": "file-list",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {
                                "filenames": [],
                                "paths": []
                            }
                        },
                        {
                            "zh-name": "分波态密度",
                            "tag_name": "Fractional_density_of_states",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "d带中心",
                            "tag_name": "dband_center",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        }
                    ]
                },
                {
                    "zh-name": "能带",
                    "tag_name": "Band",
                    "type": "container",
                    "children": [
                        {
                            "zh-name": "带隙",
                            "tag_name": "Bandgap",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": " 电子结构",
                            "tag_name": "electronic_structure",
                            "type": "file-list",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {
                                "filenames": [],
                                "paths": []
                            }
                        }
                    ]
                },
                {
                    "zh-name": "磁性",
                    "tag_name": "magnetic",
                    "type": "container",
                    "children": [
                        {
                            "zh-name": "有无磁性",
                            "tag_name": "With_or_without_magnetism",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        },
                        {
                            "zh-name": "总磁矩 ",
                            "tag_name": "total_magnetic_moment",
                            "type": "uncheck-stringtype",
                            "default": "",
                            "path": "",
                            "xpath": "",
                            "callback": "",
                            "kwargs": {}
                        }
                    ]
                }
            ]
        }
    ]
}