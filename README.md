# 第一性原理VASP计算数据自动提取

## 流程介绍

我们提取的数据**基本**都来自于 `vasprun.xml`，我们的目的就是从这个xml文件中用xpath提取数据并生成符合实验室平台模板的xml

 `config.py` 是一个实验室模板的json形式，我们需要在这里配置每个字段的xpath，以及对应的callback（如果需要的话）来提取数据

我在 `config.py` 中已经写了个两个字段的配置供参考，分别是 calculating_time 和 Optimized_unit_cell_parameters, calculating_time在 `vasprun.xml` 中的xpath是 `.//generator/i[@name='date']`, 这个比较好理解，程序会自动根据这个 xpath 在 path指向的文件中进行匹配，返回的是一个list，但如果list只有一个数据，就返回list的第0个元素

Optimized_unit_cell_parameters 是一个3x3的表格，他对应的 xpath 是 `.//structure/crystal/varray[@name='basis']/v`, 提取得到的结果是一个长度为3的list，所以我们需要编写一个callback函数提取的结果进行处理，这个callback在 `utils/callbacks.optimized_unit_cell_parameters_callback` 中，所有的callback函数都有两个参数，分别是 `res_list` 和 `kwargs`, `rest_list`是xpath匹配到的结果， `kwargs` 则是 `config.py` 中的`kwargs`。

所以要做的就是:

1. 查看xmind中需要提取的vasp软件的字段
2. 在config中编写这个字段的xpath
3. 如果需要后处理在 `utils.callbacks` 下编写回调函数，并填写在 `config` 里
4. 运行 `main.py` 生成结果，检查一下是否提取成功
   

## 测试流程

编写完成 `config.py` 运行一下 `main.py`，会在 `outputs` 下生成结果，你可以在这看是否提取成功

需要注意的是，这里只提供了一个 `vasprun.xml` ，为了考虑到意外情况最好多测试几个 `vasprun.xml`