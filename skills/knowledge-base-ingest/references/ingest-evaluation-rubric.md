# Ingest Evaluation Rubric

用于比较**候选结构**和**当前稳定基线**，决定这一轮 ingest 调整是否值得保留。

## 评分关注点

1. 拆分适配度  
2. 页面角色清晰度  
3. 检索友好度  
4. 导航覆盖度  
5. 关联链接有效性  
6. 来源链与入口同步  
7. 回归稳定性  

## 使用方式

- 每轮优先只改一类结构问题
- 用同一口径比较 baseline 和 candidate
- 如果 candidate 总体更好且没有关键回归，再晋升为新的 baseline

## 不应晋升的情况

- 总分没有提高
- root page / reader entrypoint / source lineage 变弱
- 引入新的 orphan pages / dead links
- 页面角色明显更混乱

## 最小结论格式

- baseline 有什么问题
- candidate 改了什么
- 哪些维度确实变好
- 是否通过回归检查
- promote / rework / drop
