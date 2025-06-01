# GenEval Evaluation Report

**Model:** Flymy AI
**Evaluation Date:** 2025-06-01 18:02:49
**Data Source:** `../../../../output/flymy_geneval/sample_eval/results_full.jsonl`

## Summary Results

| Metric | Value |
|--------|--------|
| **Overall Image Accuracy** | 76.16% (1680/2206) |
| **Prompt Accuracy** | 60.69% (335/552) |
| **Total Categories** | 6 |
| **Overall Score** | 0.7690 |

**Overall Performance Rating:** Good

## Category Breakdown

### POSITION: Spatial positioning of objects

- **Accuracy:** 50.50% (202/400)
- **Prompts:** 100
- **Images per Prompt:** 4
- **Example Prompts:**
  - "a photo of a dog above a cow"
  - "a photo of a bus above a boat"
  - "a photo of a pizza right of a banana"

### COLOR_ATTR: color_attr

- **Accuracy:** 57.75% (231/400)
- **Prompts:** 100
- **Images per Prompt:** 4
- **Example Prompts:**
  - "a photo of a yellow dining table and a pink dog"
  - "a photo of a pink skateboard and a black train"
  - "a photo of a brown bed and a pink cell phone"

### COUNTING: Object counting accuracy (2-4 items)

- **Accuracy:** 70.31% (225/320)
- **Prompts:** 80
- **Images per Prompt:** 4
- **Example Prompts:**
  - "a photo of two vases"
  - "a photo of two tv remotes"
  - "a photo of four microwaves"

### COLORS: Object color specification

- **Accuracy:** 86.02% (320/372)
- **Prompts:** 93
- **Images per Prompt:** 4
- **Example Prompts:**
  - "a photo of a blue cow"
  - "a photo of a pink skateboard"
  - "a photo of a white teddy bear"

### TWO_OBJECT: Two objects generation

- **Accuracy:** 97.46% (384/394)
- **Prompts:** 99
- **Images per Prompt:** 3
- **Example Prompts:**
  - "a photo of a tennis racket and a wine glass"
  - "a photo of a tennis racket and a bird"
  - "a photo of a giraffe and a computer mouse"

### SINGLE_OBJECT: Single object generation

- **Accuracy:** 99.38% (318/320)
- **Prompts:** 80
- **Images per Prompt:** 4
- **Example Prompts:**
  - "a photo of a vase"
  - "a photo of a sandwich"
  - "a photo of a carrot"

## Error Analysis

| Error Type | Count |
|------------|-------|
| expected bed right of target, found  target | 7 |
| expected brown car>=1, found 0 brown; and 1 orange | 7 |
| expected toothbrush>=1, found 0 | 6 |
| expected tie right of target, found  target | 5 |
| expected cat below target, found  target | 5 |
| expected orange<4, found 4 | 4 |
| expected kite>=1, found 0 | 4 |
| expected carrot>=1, found 0 | 4 |
| expected red giraffe>=1, found 0 red; and 1 brown | 4 |
| expected yellow orange>=1, found 0 yellow; and 1 orange | 4 |
| expected brown orange>=1, found 0 brown; and 1 orange | 4 |
| expected white orange>=1, found 0 white; and 1 orange | 4 |
| expected laptop left of target, found  target | 4 |
| expected train right of target, found above target | 4 |
| expected knife right of target, found  target | 4 |
| expected tie above target, found  target | 4 |
| expected bird left of target, found  target | 4 |
| expected cup left of target, found below target | 4 |
| expected zebra below target, found above target | 4 |
| expected baseball bat>=1, found 0
no target for refrigerator to be above | 4 |
| expected refrigerator below target, found  target | 4 |
| expected cow right of target, found  target | 4 |
| expected black broccoli>=1, found 0 black; and 1 green | 4 |
| expected black dining table>=1, found 0 black; and 1 purple | 4 |
| expected brown carrot>=1, found 0 brown; and 1 orange
expected white potted plant>=1, found 0 white; and 1 green | 4 |
| expected brown hot dog>=1, found 0 brown; and 1 yellow | 4 |
| expected green carrot>=1, found 0 green; and 1 orange | 4 |
| expected white stop sign>=1, found 0 white; and 1 red | 4 |
| expected red orange>=1, found 0 red; and 1 orange | 4 |
| expected baseball bat>=1, found 0 | 3 |
| expected sports ball<4, found 4 | 3 |
| expected handbag<4, found 4 | 3 |
| expected book<5, found 8 | 3 |
| expected blue carrot>=1, found 0 blue; and 1 orange | 3 |
| expected dog above target, found  target | 3 |
| expected dining table right of target, found below target | 3 |
| expected tv remote left of target, found below target | 3 |
| expected sports ball left of target, found  target | 3 |
| expected computer mouse left of target, found  target | 3 |
| expected hot dog right of target, found above target | 3 |
| expected suitcase above target, found left of target | 3 |
| expected kite>=1, found 0
no target for toilet to be left of | 3 |
| expected elephant below target, found left of target | 3 |
| expected truck left of target, found above target | 3 |
| expected frisbee right of target, found below target | 3 |
| expected donut right of target, found  target | 3 |
| expected snowboard>=1, found 0
no target for computer keyboard to be above | 3 |
| expected tv below target, found  target | 3 |
| expected suitcase left of target, found below target | 3 |
| expected laptop right of target, found below target | 3 |
| expected cell phone right of target, found  target | 3 |
| expected couch below target, found right of target | 3 |
| expected white handbag>=1, found 0 white; and 1 purple | 3 |
| expected white pizza>=1, found 0 white; and 1 green | 3 |
| expected brown bed>=1, found 0 brown; and 1 pink | 3 |
| expected black spoon>=1, found 0 black; and 1 brown | 3 |
| expected yellow pizza>=1, found 0 yellow; and 1 white | 3 |
| expected black potted plant>=1, found 0 black; and 1 green | 3 |
| expected white umbrella>=1, found 0 white; and 1 purple | 3 |
| expected pink broccoli>=1, found 0 pink; and 1 green | 3 |
| expected orange giraffe>=1, found 0 orange; and 1 brown
expected white baseball glove>=1, found 0 white; and 1 brown | 3 |
| expected red pizza>=1, found 0 red; and 1 white | 3 |
| expected sink>=1, found 0 | 2 |
| expected computer mouse>=1, found 0 | 2 |
| expected frisbee>=1, found 0 | 2 |
| expected bowl>=1, found 0 | 2 |
| expected frisbee<3, found 3 | 2 |
| expected tie<3, found 3 | 2 |
| expected sink>=4, found 2 | 2 |
| expected toothbrush<3, found 3 | 2 |
| expected vase<5, found 5 | 2 |
| expected sink>=3, found 2 | 2 |
| expected bicycle>=2, found 1 | 2 |
| expected hot dog>=3, found 2 | 2 |
| expected book<4, found 4 | 2 |
| expected book<4, found 5 | 2 |
| expected sandwich>=2, found 1 | 2 |
| expected traffic light>=4, found 2 | 2 |
| expected banana>=2, found 1 | 2 |
| expected banana>=2, found 0 | 2 |
| expected pizza<4, found 4 | 2 |
| expected suitcase<4, found 5 | 2 |
| expected hot dog>=4, found 2 | 2 |
| expected hot dog>=4, found 3 | 2 |
| expected bench>=3, found 1 | 2 |
| expected white sandwich>=1, found 0 white; and 1 yellow | 2 |
| expected red dog>=1, found 0 red; and 1 orange | 2 |
| expected red dog>=1, found 0 red; and 1 brown | 2 |
| expected black train>=1, found 0 black; and 1 red | 2 |
| expected white sheep>=1, found 0 white; and 1 brown | 2 |
| expected yellow broccoli>=1, found 0 yellow; and 1 green | 2 |
| expected wine glass above target, found below target | 2 |
| expected wine glass above target, found left of target | 2 |
| expected fork above target, found  target | 2 |
| expected fork>=1, found 0
no target for stop sign to be above | 2 |
| expected truck left of target, found  target | 2 |
| expected bottle right of target, found  target | 2 |
| expected hot dog left of target, found above target | 2 |
| expected backpack right of target, found  target | 2 |
| expected hair drier>=1, found 0 | 2 |
| expected hair drier below target, found  target | 2 |
| expected book above target, found  target | 2 |
| expected laptop below target, found  target | 2 |
| expected dining table above target, found  target | 2 |
| expected pizza right of target, found below target | 2 |
| expected bench left of target, found  target | 2 |
| expected zebra right of target, found  target | 2 |
| expected backpack below target, found left of target | 2 |
| expected black apple>=1, found 0 black; and 1 purple | 2 |
| expected green skis>=1, found 0 green; and 1 black
expected brown airplane>=1, found 0 brown; and 1 orange | 2 |
| expected black sink>=1, found 0 black; and 1 purple | 2 |
| expected black banana>=1, found 0 black; and 1 blue | 2 |
| expected black scissors>=1, found 0 black; and 1 pink | 2 |
| expected orange snowboard>=1, found 0 orange; and 1 black | 2 |
| expected white wine glass>=1, found 0 white; and 1 black | 2 |
| expected white boat>=1, found 0 white; and 1 yellow
expected orange hot dog>=1, found 0 orange; and 1 yellow | 2 |
| expected black spoon>=1, found 0 black; and 1 blue | 2 |
| expected blue potted plant>=1, found 0 blue; and 1 green | 2 |
| expected brown oven>=1, found 0 brown; and 1 purple | 2 |
| expected black car>=1, found 0 black; and 1 white | 2 |
| expected black cell phone>=1, found 0 black; and 1 blue | 2 |
| expected white toilet>=1, found 0 white; and 1 brown | 2 |
| expected backpack>=1, found 0 | 1 |
| expected bench>=1, found 0 | 1 |
| expected clock<3, found 3 | 1 |
| expected backpack>=2, found 0 | 1 |
| expected frisbee<3, found 4 | 1 |
| expected tie>=2, found 1 | 1 |
| expected sink>=4, found 3 | 1 |
| expected sink>=4, found 1 | 1 |
| expected computer keyboard<5, found 6 | 1 |
| expected computer keyboard>=4, found 3 | 1 |
| expected bicycle<3, found 3 | 1 |
| expected train<3, found 4 | 1 |
| expected train>=2, found 1 | 1 |
| expected apple>=3, found 1 | 1 |
| expected apple>=3, found 2 | 1 |
| expected apple<4, found 5 | 1 |
| expected apple<5, found 5 | 1 |
| expected apple>=4, found 3 | 1 |
| expected computer keyboard<4, found 4 | 1 |
| expected baseball bat>=3, found 1 | 1 |
| expected baseball bat<4, found 5 | 1 |
| expected baseball bat<4, found 4 | 1 |
| expected stop sign>=4, found 3 | 1 |
| expected pizza>=2, found 0 | 1 |
| expected pizza>=2, found 1 | 1 |
| expected pizza<3, found 3 | 1 |
| expected refrigerator>=3, found 2 | 1 |
| expected broccoli>=4, found 1 | 1 |
| expected carrot<3, found 3 | 1 |
| expected traffic light>=4, found 0 | 1 |
| expected traffic light>=4, found 3 | 1 |
| expected car<3, found 5 | 1 |
| expected wine glass<3, found 4 | 1 |
| expected suitcase<4, found 4 | 1 |
| expected skateboard<5, found 5 | 1 |
| expected boat<5, found 5 | 1 |
| expected boat<5, found 6 | 1 |
| expected parking meter<3, found 3 | 1 |
| expected bench<5, found 6 | 1 |
| expected bench>=4, found 2 | 1 |
| expected bench>=4, found 3 | 1 |
| expected bench>=3, found 2 | 1 |
| expected bench<4, found 6 | 1 |
| expected frisbee<5, found 5 | 1 |
| expected book<5, found 6 | 1 |
| expected bus>=4, found 3 | 1 |
| expected red bicycle>=1, found 0 red; and 1 pink | 1 |
| expected white sandwich>=1, found 0 white; and 1 brown | 1 |
| expected brown computer keyboard>=1, found 0 brown; and 1 black | 1 |
| expected brown skis>=1, found 0 brown; and 1 black | 1 |
| expected brown skis>=1, found 0 brown; and 1 white | 1 |
| expected skis>=1, found 0 | 1 |
| expected white scissors>=1, found 0 white; and 1 yellow | 1 |
| expected white scissors>=1, found 0 white; and 1 pink | 1 |
| expected white scissors>=1, found 0 white; and 1 orange | 1 |
| expected purple carrot>=1, found 0 purple; and 1 brown | 1 |
| expected pink potted plant>=1, found 0 pink; and 1 green | 1 |
| expected green hot dog>=1, found 0 green; and 1 yellow | 1 |
| expected red potted plant>=1, found 0 red; and 1 brown | 1 |
| expected brown refrigerator>=1, found 0 brown; and 1 green | 1 |
| expected black tv remote>=1, found 0 black; and 1 blue | 1 |
| expected parking meter>=1, found 0 | 1 |
| expected white sheep>=1, found 0 white; and 1 green | 1 |
| expected yellow carrot>=1, found 0 yellow; and 1 orange | 1 |
| expected black hot dog>=1, found 0 black; and 1 yellow | 1 |
| expected blue book>=1, found 0 blue; and 1 brown | 1 |
| expected bird below target, found above target | 1 |
| expected apple above target, found  target | 1 |
| expected apple above target, found below target | 1 |
| expected tv remote below target, found left of target | 1 |
| expected skateboard above target, found left of target | 1 |
| expected dining table right of target, found  target | 1 |
| expected hot dog left of target, found  target | 1 |
| expected hot dog left of target, found below target | 1 |
| expected toothbrush>=1, found 0
no target for bus to be below | 1 |
| expected bus below target, found  target | 1 |
| expected bus below target, found left of target | 1 |
| expected backpack right of target, found above target | 1 |
| expected baseball bat>=1, found 0
no target for cake to be below | 1 |
| expected dog right of target, found above target | 1 |
| expected dog right of target, found  target | 1 |
| expected suitcase right of target, found  target | 1 |
| expected suitcase right of target, found below target | 1 |
| expected sports ball left of target, found below target | 1 |
| expected wine glass right of target, found  target | 1 |
| expected toothbrush>=1, found 0
no target for kite to be above | 1 |
| expected cat below target, found right of target | 1 |
| expected hot dog right of target, found  target | 1 |
| expected hair drier left of target, found  target | 1 |
| expected cow left of target, found right of target | 1 |
| expected book above target, found right of target | 1 |
| expected book above target, found below target | 1 |
| expected toilet left of target, found below target | 1 |
| expected hot dog above target, found  target | 1 |
| expected bed right of target, found above target | 1 |
| expected laptop below target, found right of target | 1 |
| expected vase>=1, found 0 | 1 |
| expected parking meter above target, found  target | 1 |
| expected parking meter above target, found left of target | 1 |
| expected parking meter above target, found right of target | 1 |
| expected pizza right of target, found left of target | 1 |
| expected bench left of target, found right of target | 1 |
| expected donut right of target, found below target | 1 |
| expected cell phone left of target, found right of target | 1 |
| expected vase right of target, found below target | 1 |
| expected bear above target, found  target | 1 |
| expected zebra right of target, found above target | 1 |
| expected elephant below target, found  target | 1 |
| expected suitcase left of target, found above target | 1 |
| expected tie right of target, found above target | 1 |
| expected tv>=1, found 0
no target for laptop to be right of | 1 |
| expected cell phone right of target, found below target | 1 |
| expected backpack below target, found  target | 1 |
| expected bicycle above target, found  target | 1 |
| expected apple>=1, found 0 | 1 |
| expected purple wine glass>=1, found 0 purple; and 1 red
expected black apple>=1, found 0 black; and 1 purple | 1 |
| expected green bus>=1, found 0 green; and 1 pink | 1 |
| expected brown airplane>=1, found 0 brown; and 1 green | 1 |
| expected green skis>=1, found 0 green; and 1 black | 1 |
| expected brown tie>=1, found 0 brown; and 1 red | 1 |
| expected red skis>=1, found 0 red; and 1 brown | 1 |
| expected brown sports ball>=1, found 0 brown; and 1 purple | 1 |
| expected white dining table>=1, found 0 white; and 1 red | 1 |
| expected black banana>=1, found 0 black; and 1 green | 1 |
| expected orange potted plant>=1, found 0 orange; and 1 red | 1 |
| expected black kite>=1, found 0 black; and 1 blue | 1 |
| expected brown bear>=1, found 0 brown; and 1 blue | 1 |
| expected black scissors>=1, found 0 black; and 1 blue | 1 |
| expected brown kite>=1, found 0 brown; and 1 orange | 1 |
| expected green teddy bear>=1, found 0 green; and 1 brown | 1 |
| expected yellow stop sign>=1, found 0 yellow; and 1 orange | 1 |
| expected yellow stop sign>=1, found 0 yellow; and 1 pink | 1 |
| expected brown cell phone>=1, found 0 brown; and 1 purple | 1 |
| expected brown cell phone>=1, found 0 brown; and 1 orange | 1 |
| expected sheep>=1, found 0 | 1 |
| expected white cell phone>=1, found 0 white; and 1 blue | 1 |
| expected tie>=1, found 0 | 1 |
| expected white tie>=1, found 0 white; and 1 blue | 1 |
| expected brown bed>=1, found 0 brown; and 1 pink
expected cell phone>=1, found 0 | 1 |
| expected suitcase>=1, found 0 | 1 |
| expected sports ball>=1, found 0
expected green boat>=1, found 0 green; and 1 blue | 1 |
| expected white wine glass>=1, found 0 white; and 1 brown | 1 |
| expected white boat>=1, found 0 white; and 1 yellow | 1 |
| expected orange hot dog>=1, found 0 orange; and 1 yellow | 1 |
| expected orange skateboard>=1, found 0 orange; and 1 brown | 1 |
| expected black computer keyboard>=1, found 0 black; and 1 blue | 1 |
| expected black bottle>=1, found 0 black; and 1 white | 1 |
| expected white refrigerator>=1, found 0 white; and 1 brown | 1 |
| expected book>=1, found 0 | 1 |
| expected yellow pizza>=1, found 0 yellow; and 1 green | 1 |
| expected brown car>=1, found 0 brown; and 1 red | 1 |
| expected brown dining table>=1, found 0 brown; and 1 white | 1 |
| expected white suitcase>=1, found 0 white; and 1 brown | 1 |
| expected orange donut>=1, found 0 orange; and 1 pink
expected stop sign>=1, found 0 | 1 |
| expected blue scissors>=1, found 0 blue; and 1 purple | 1 |
| expected black cell phone>=1, found 0 black; and 1 brown | 1 |
| expected blue baseball bat>=1, found 0 blue; and 1 pink | 1 |
| expected orange pizza>=1, found 0 orange; and 1 green | 1 |
| expected orange pizza>=1, found 0 orange; and 1 white | 1 |
| expected orange pizza>=1, found 0 orange; and 1 yellow | 1 |
| expected orange pizza>=1, found 0 orange; and 1 purple | 1 |
| expected yellow suitcase>=1, found 0 yellow; and 1 brown
expected brown bus>=1, found 0 brown; and 1 orange | 1 |
| expected brown bus>=1, found 0 brown; and 1 red | 1 |
| expected brown bus>=1, found 0 brown; and 1 orange | 1 |
| expected white bottle>=1, found 0 white; and 1 blue | 1 |
| expected refrigerator>=1, found 0 | 1 |
| expected pink broccoli>=1, found 0 pink; and 1 green
expected red sink>=1, found 0 red; and 1 pink | 1 |
| expected white toilet>=1, found 0 white; and 1 pink | 1 |
| expected orange giraffe>=1, found 0 orange; and 1 brown | 1 |
| expected pink dining table>=1, found 0 pink; and 1 black | 1 |
| expected black car>=1, found 0 black; and 1 green | 1 |
| expected white banana>=1, found 0 white; and 1 brown
expected black elephant>=1, found 0 black; and 1 brown | 1 |
| expected white banana>=1, found 0 white; and 1 yellow | 1 |
| expected white banana>=1, found 0 white; and 1 brown | 1 |
| expected orange cow>=1, found 0 orange; and 1 purple | 1 |
| expected black cell phone>=1, found 0 black; and 1 red | 1 |
| expected brown knife>=1, found 0 brown; and 1 blue | 1 |
| expected yellow bicycle>=1, found 0 yellow; and 1 black
expected red motorcycle>=1, found 0 red; and 1 yellow | 1 |
| expected bicycle>=1, found 0
expected red motorcycle>=1, found 0 red; and 1 yellow | 1 |
| expected orange traffic light>=1, found 0 orange; and 1 brown
expected white toilet>=1, found 0 white; and 1 brown | 1 |
| expected red pizza>=1, found 0 red; and 1 orange | 1 |

## Prompt Analysis

| Prompt | Success Rate | Images |
|--------|--------------|--------|
| a photo of four sinks | 0.0% (0/4) | 4 |
| a photo of three oranges | 0.0% (0/4) | 4 |
| a photo of three books | 0.0% (0/4) | 4 |
| a photo of four traffic lights | 0.0% (0/4) | 4 |
| a photo of two bananas | 0.0% (0/4) | 4 |
| a photo of four hot dogs | 0.0% (0/4) | 4 |
| a photo of three benchs | 0.0% (0/4) | 4 |
| a photo of four books | 0.0% (0/4) | 4 |
| a photo of a red dog | 0.0% (0/4) | 4 |
| a photo of a purple carrot | 0.0% (0/4) | 4 |
| a photo of a yellow orange | 0.0% (0/4) | 4 |
| a photo of a brown orange | 0.0% (0/4) | 4 |
| a photo of a white orange | 0.0% (0/4) | 4 |
| a photo of a blue carrot | 0.0% (0/4) | 4 |
| a photo of a wine glass above a kite | 0.0% (0/4) | 4 |
| a photo of a laptop left of a cow | 0.0% (0/4) | 4 |
| a photo of a dining table right of an oven | 0.0% (0/4) | 4 |
| a photo of a hot dog left of a suitcase | 0.0% (0/4) | 4 |
| a photo of a sports ball left of an umbrella | 0.0% (0/4) | 4 |
| a photo of a train right of a dining table | 0.0% (0/4) | 4 |
| a photo of a hot dog right of a skateboard | 0.0% (0/4) | 4 |
| a photo of a book above a laptop | 0.0% (0/4) | 4 |
| a photo of a toothbrush below a pizza | 0.0% (0/4) | 4 |
| a photo of a toilet left of a kite | 0.0% (0/4) | 4 |
| a photo of a knife right of a suitcase | 0.0% (0/4) | 4 |
| a photo of a tie above a sink | 0.0% (0/4) | 4 |
| a photo of a bird left of a couch | 0.0% (0/4) | 4 |
| a photo of a bed right of a sports ball | 0.0% (0/4) | 4 |
| a photo of a cup left of an umbrella | 0.0% (0/4) | 4 |
| a photo of a zebra below a computer keyboard | 0.0% (0/4) | 4 |
| a photo of a truck left of a baseball bat | 0.0% (0/4) | 4 |
| a photo of a refrigerator above a baseball bat | 0.0% (0/4) | 4 |
| a photo of a frisbee right of a motorcycle | 0.0% (0/4) | 4 |
| a photo of a refrigerator below a scissors | 0.0% (0/4) | 4 |
| a photo of a donut right of a bench | 0.0% (0/4) | 4 |
| a photo of a cow right of a laptop | 0.0% (0/4) | 4 |
| a photo of a bed right of a frisbee | 0.0% (0/4) | 4 |
| a photo of a suitcase left of a banana | 0.0% (0/4) | 4 |
| a photo of a laptop right of a tv | 0.0% (0/4) | 4 |
| a photo of a cell phone right of a chair | 0.0% (0/4) | 4 |
| a photo of a cat below a backpack | 0.0% (0/4) | 4 |
| a photo of a purple wine glass and a black apple | 0.0% (0/4) | 4 |
| a photo of a green skis and a brown airplane | 0.0% (0/4) | 4 |
| a photo of a black broccoli and a yellow cake | 0.0% (0/4) | 4 |
| a photo of a purple dog and a black dining table | 0.0% (0/4) | 4 |
| a photo of a brown carrot and a white potted plant | 0.0% (0/4) | 4 |
| a photo of a black kite and a green bear | 0.0% (0/4) | 4 |
| a photo of a brown car and a pink hair drier | 0.0% (0/4) | 4 |
| a photo of a brown hot dog and a purple pizza | 0.0% (0/4) | 4 |
| a photo of a brown bed and a pink cell phone | 0.0% (0/4) | 4 |
| a photo of a white boat and an orange hot dog | 0.0% (0/4) | 4 |
| a photo of an orange handbag and a green carrot | 0.0% (0/4) | 4 |
| a photo of a yellow pizza and a green oven | 0.0% (0/4) | 4 |
| a photo of a red laptop and a brown car | 0.0% (0/4) | 4 |
| a photo of a purple suitcase and an orange pizza | 0.0% (0/4) | 4 |
| a photo of a pink broccoli and a red sink | 0.0% (0/4) | 4 |
| a photo of an orange giraffe and a white baseball glove | 0.0% (0/4) | 4 |
| a photo of a brown giraffe and a white stop sign | 0.0% (0/4) | 4 |
| a photo of a red orange and a purple broccoli | 0.0% (0/4) | 4 |
| a photo of a green cup and a red pizza | 0.0% (0/4) | 4 |
| a photo of two frisbees | 25.0% (1/4) | 4 |
| a photo of three sports balls | 25.0% (1/4) | 4 |
| a photo of two ties | 25.0% (1/4) | 4 |
| a photo of two bicycles | 25.0% (1/4) | 4 |
| a photo of three handbags | 25.0% (1/4) | 4 |
| a photo of three apples | 25.0% (1/4) | 4 |
| a photo of three baseball bats | 25.0% (1/4) | 4 |
| a photo of two pizzas | 25.0% (1/4) | 4 |
| a photo of three suitcases | 25.0% (1/4) | 4 |
| a photo of four benchs | 25.0% (1/4) | 4 |
| a photo of a white sandwich | 25.0% (1/4) | 4 |
| a photo of a brown skis | 25.0% (1/4) | 4 |
| a photo of a white scissors | 25.0% (1/4) | 4 |
| a photo of a white sheep | 25.0% (1/4) | 4 |
| a photo of a tie right of a baseball bat | 25.0% (1/4) | 4 |
| a photo of a dog above a cow | 25.0% (1/4) | 4 |
| a photo of a bus below a toothbrush | 25.0% (1/4) | 4 |
| a photo of a backpack right of a sandwich | 25.0% (1/4) | 4 |
| a photo of a tv remote left of an umbrella | 25.0% (1/4) | 4 |
| a photo of a hair drier below an elephant | 25.0% (1/4) | 4 |
| a photo of a computer mouse left of a bench | 25.0% (1/4) | 4 |
| a photo of a suitcase above a skis | 25.0% (1/4) | 4 |
| a photo of a laptop below a sports ball | 25.0% (1/4) | 4 |
| a photo of a parking meter above a broccoli | 25.0% (1/4) | 4 |
| a photo of a pizza right of a banana | 25.0% (1/4) | 4 |
| a photo of a bench left of a bear | 25.0% (1/4) | 4 |
| a photo of a computer keyboard above a snowboard | 25.0% (1/4) | 4 |
| a photo of a tv below a cow | 25.0% (1/4) | 4 |
| a photo of a zebra right of a bed | 25.0% (1/4) | 4 |
| a photo of a tie right of a motorcycle | 25.0% (1/4) | 4 |
| a photo of a couch below a potted plant | 25.0% (1/4) | 4 |
| a photo of a backpack below a cake | 25.0% (1/4) | 4 |
| a photo of a white handbag and a purple bed | 25.0% (1/4) | 4 |
| a photo of a blue vase and a black banana | 25.0% (1/4) | 4 |
| a photo of a pink handbag and a black scissors | 25.0% (1/4) | 4 |
| a photo of a white pizza and a green umbrella | 25.0% (1/4) | 4 |
| a photo of a white wine glass and a brown giraffe | 25.0% (1/4) | 4 |
| a photo of an orange microwave and a black spoon | 25.0% (1/4) | 4 |
| a photo of a black potted plant and a yellow toilet | 25.0% (1/4) | 4 |
| a photo of a yellow suitcase and a brown bus | 25.0% (1/4) | 4 |
| a photo of a purple backpack and a white umbrella | 25.0% (1/4) | 4 |
| a photo of a black car and a green parking meter | 25.0% (1/4) | 4 |
| a photo of a white banana and a black elephant | 25.0% (1/4) | 4 |
| a photo of a red clock and a black cell phone | 25.0% (1/4) | 4 |
| a photo of an orange traffic light and a white toilet | 25.0% (1/4) | 4 |
| a photo of a toilet and a computer mouse | 50.0% (2/4) | 4 |
| a photo of a baseball bat and a giraffe | 50.0% (2/4) | 4 |
| a photo of two toothbrushs | 50.0% (2/4) | 4 |
| a photo of four vases | 50.0% (2/4) | 4 |
| a photo of four computer keyboards | 50.0% (2/4) | 4 |
| a photo of three sinks | 50.0% (2/4) | 4 |
| a photo of two trains | 50.0% (2/4) | 4 |
| a photo of three hot dogs | 50.0% (2/4) | 4 |
| a photo of four apples | 50.0% (2/4) | 4 |
| a photo of two sandwichs | 50.0% (2/4) | 4 |
| a photo of three pizzas | 50.0% (2/4) | 4 |
| a photo of four boats | 50.0% (2/4) | 4 |
| a photo of a yellow broccoli | 50.0% (2/4) | 4 |
| a photo of a fork above a hair drier | 50.0% (2/4) | 4 |
| a photo of a stop sign above a fork | 50.0% (2/4) | 4 |
| a photo of an apple above a tv | 50.0% (2/4) | 4 |
| a photo of a bottle right of a train | 50.0% (2/4) | 4 |
| a photo of a dog right of a tie | 50.0% (2/4) | 4 |
| a photo of a suitcase right of a boat | 50.0% (2/4) | 4 |
| a photo of a cat below a baseball glove | 50.0% (2/4) | 4 |
| a photo of a hair drier left of a toilet | 50.0% (2/4) | 4 |
| a photo of an elephant below a surfboard | 50.0% (2/4) | 4 |
| a photo of a dining table above a suitcase | 50.0% (2/4) | 4 |
| a photo of an elephant below a horse | 50.0% (2/4) | 4 |
| a photo of a red skis and a brown tie | 50.0% (2/4) | 4 |
| a photo of a purple tennis racket and a black sink | 50.0% (2/4) | 4 |
| a photo of a white handbag and a red giraffe | 50.0% (2/4) | 4 |
| a photo of a green teddy bear and a brown kite | 50.0% (2/4) | 4 |
| a photo of a yellow stop sign and a blue potted plant | 50.0% (2/4) | 4 |
| a photo of a black bus and a brown cell phone | 50.0% (2/4) | 4 |
| a photo of an orange snowboard and a green cat | 50.0% (2/4) | 4 |
| a photo of a white tie and a purple skateboard | 50.0% (2/4) | 4 |
| a photo of a black bottle and a white refrigerator | 50.0% (2/4) | 4 |
| a photo of a white dog and a blue potted plant | 50.0% (2/4) | 4 |
| a photo of a brown dining table and a white suitcase | 50.0% (2/4) | 4 |
| a photo of a red giraffe and a black cell phone | 50.0% (2/4) | 4 |
| a photo of a brown oven and a purple train | 50.0% (2/4) | 4 |
| a photo of an orange potted plant and a black spoon | 50.0% (2/4) | 4 |
| a photo of a yellow bicycle and a red motorcycle | 50.0% (2/4) | 4 |
| a photo of a backpack | 75.0% (3/4) | 4 |
| a photo of a sink | 75.0% (3/4) | 4 |
| a photo of a toothbrush and a snowboard | 75.0% (3/4) | 4 |
| a photo of a frisbee and a vase | 75.0% (3/4) | 4 |
| a photo of a toothbrush and a carrot | 75.0% (3/4) | 4 |
| a photo of a bowl and a pizza | 75.0% (3/4) | 4 |
| a photo of a baseball bat and a bear | 75.0% (3/4) | 4 |
| a photo of a microwave and a bench | 75.0% (3/4) | 4 |
| a photo of two clocks | 75.0% (3/4) | 4 |
| a photo of two backpacks | 75.0% (3/4) | 4 |
| a photo of three computer keyboards | 75.0% (3/4) | 4 |
| a photo of four stop signs | 75.0% (3/4) | 4 |
| a photo of three refrigerators | 75.0% (3/4) | 4 |
| a photo of four broccolis | 75.0% (3/4) | 4 |
| a photo of two carrots | 75.0% (3/4) | 4 |
| a photo of two cars | 75.0% (3/4) | 4 |
| a photo of two wine glasses | 75.0% (3/4) | 4 |
| a photo of four skateboards | 75.0% (3/4) | 4 |
| a photo of two parking meters | 75.0% (3/4) | 4 |
| a photo of four frisbees | 75.0% (3/4) | 4 |
| a photo of four buses | 75.0% (3/4) | 4 |
| a photo of a red bicycle | 75.0% (3/4) | 4 |
| a photo of a brown computer keyboard | 75.0% (3/4) | 4 |
| a photo of a white kite | 75.0% (3/4) | 4 |
| a photo of a pink potted plant | 75.0% (3/4) | 4 |
| a photo of a red giraffe | 75.0% (3/4) | 4 |
| a photo of a black train | 75.0% (3/4) | 4 |
| a photo of a green hot dog | 75.0% (3/4) | 4 |
| a photo of a red potted plant | 75.0% (3/4) | 4 |
| a photo of a brown refrigerator | 75.0% (3/4) | 4 |
| a photo of a black tv remote | 75.0% (3/4) | 4 |
| a photo of a red parking meter | 75.0% (3/4) | 4 |
| a photo of a yellow carrot | 75.0% (3/4) | 4 |
| a photo of a black hot dog | 75.0% (3/4) | 4 |
| a photo of a blue book | 75.0% (3/4) | 4 |
| a photo of a bird below a skateboard | 75.0% (3/4) | 4 |
| a photo of a truck left of a refrigerator | 75.0% (3/4) | 4 |
| a photo of a tv remote below a cow | 75.0% (3/4) | 4 |
| a photo of a skateboard above a person | 75.0% (3/4) | 4 |
| a photo of a cake below a baseball bat | 75.0% (3/4) | 4 |
| a photo of a wine glass right of a hot dog | 75.0% (3/4) | 4 |
| a photo of a kite above a toothbrush | 75.0% (3/4) | 4 |
| a photo of a cow left of a stop sign | 75.0% (3/4) | 4 |
| a photo of a hot dog above a knife | 75.0% (3/4) | 4 |
| a photo of a vase above a fire hydrant | 75.0% (3/4) | 4 |
| a photo of a cell phone left of a tennis racket | 75.0% (3/4) | 4 |
| a photo of a vase right of a horse | 75.0% (3/4) | 4 |
| a photo of a bear above a spoon | 75.0% (3/4) | 4 |
| a photo of a bicycle above a parking meter | 75.0% (3/4) | 4 |
| a photo of a green bus and a purple microwave | 75.0% (3/4) | 4 |
| a photo of a yellow computer keyboard and a black sink | 75.0% (3/4) | 4 |
| a photo of a pink skateboard and a black train | 75.0% (3/4) | 4 |
| a photo of a purple elephant and a brown sports ball | 75.0% (3/4) | 4 |
| a photo of a white dining table and a red car | 75.0% (3/4) | 4 |
| a photo of a red car and an orange potted plant | 75.0% (3/4) | 4 |
| a photo of a blue laptop and a brown bear | 75.0% (3/4) | 4 |
| a photo of a purple sheep and a pink banana | 75.0% (3/4) | 4 |
| a photo of a blue handbag and a white cell phone | 75.0% (3/4) | 4 |
| a photo of a blue toilet and a white suitcase | 75.0% (3/4) | 4 |
| a photo of a yellow sports ball and a green boat | 75.0% (3/4) | 4 |
| a photo of an orange skateboard and a pink bowl | 75.0% (3/4) | 4 |
| a photo of a blue cow and a black computer keyboard | 75.0% (3/4) | 4 |
| a photo of a red stop sign and a blue book | 75.0% (3/4) | 4 |
| a photo of an orange donut and a yellow stop sign | 75.0% (3/4) | 4 |
| a photo of a purple computer keyboard and a blue scissors | 75.0% (3/4) | 4 |
| a photo of a blue baseball bat and a pink book | 75.0% (3/4) | 4 |
| a photo of a white bottle and a blue sheep | 75.0% (3/4) | 4 |
| a photo of a yellow handbag and a blue refrigerator | 75.0% (3/4) | 4 |
| a photo of a red bowl and a pink sink | 75.0% (3/4) | 4 |
| a photo of a white toilet and a red apple | 75.0% (3/4) | 4 |
| a photo of a pink dining table and a black sandwich | 75.0% (3/4) | 4 |
| a photo of an orange cow and a purple sandwich | 75.0% (3/4) | 4 |
| a photo of a brown knife and a blue donut | 75.0% (3/4) | 4 |
| a photo of a bench | 100.0% (4/4) | 4 |
| a photo of a cow | 100.0% (4/4) | 4 |
| a photo of a bicycle | 100.0% (4/4) | 4 |
| a photo of a clock | 100.0% (4/4) | 4 |
| a photo of a carrot | 100.0% (4/4) | 4 |
| a photo of a fork | 100.0% (4/4) | 4 |
| a photo of a refrigerator | 100.0% (4/4) | 4 |
| a photo of a suitcase | 100.0% (4/4) | 4 |
| a photo of a microwave | 100.0% (4/4) | 4 |
| a photo of a snowboard | 100.0% (4/4) | 4 |
| a photo of a potted plant | 100.0% (4/4) | 4 |
| a photo of a surfboard | 100.0% (4/4) | 4 |
| a photo of a cup | 100.0% (4/4) | 4 |
| a photo of a zebra | 100.0% (4/4) | 4 |
| a photo of a parking meter | 100.0% (4/4) | 4 |
| a photo of a skateboard | 100.0% (4/4) | 4 |
| a photo of a motorcycle | 100.0% (4/4) | 4 |
| a photo of a spoon | 100.0% (4/4) | 4 |
| a photo of a car | 100.0% (4/4) | 4 |
| a photo of a traffic light | 100.0% (4/4) | 4 |
| a photo of a couch | 100.0% (4/4) | 4 |
| a photo of a tie | 100.0% (4/4) | 4 |
| a photo of a book | 100.0% (4/4) | 4 |
| a photo of a chair | 100.0% (4/4) | 4 |
| a photo of a frisbee | 100.0% (4/4) | 4 |
| a photo of a laptop | 100.0% (4/4) | 4 |
| a photo of a tv | 100.0% (4/4) | 4 |
| a photo of a computer mouse | 100.0% (4/4) | 4 |
| a photo of a computer keyboard | 100.0% (4/4) | 4 |
| a photo of a scissors | 100.0% (4/4) | 4 |
| a photo of a broccoli | 100.0% (4/4) | 4 |
| a photo of a toaster | 100.0% (4/4) | 4 |
| a photo of a sandwich | 100.0% (4/4) | 4 |
| a photo of a bottle | 100.0% (4/4) | 4 |
| a photo of a bed | 100.0% (4/4) | 4 |
| a photo of an elephant | 100.0% (4/4) | 4 |
| a photo of a toilet | 100.0% (4/4) | 4 |
| a photo of an oven | 100.0% (4/4) | 4 |
| a photo of an orange | 100.0% (4/4) | 4 |
| a photo of a person | 100.0% (4/4) | 4 |
| a photo of a baseball bat | 100.0% (4/4) | 4 |
| a photo of a bird | 100.0% (4/4) | 4 |
| a photo of a train | 100.0% (4/4) | 4 |
| a photo of a skis | 100.0% (4/4) | 4 |
| a photo of a cell phone | 100.0% (4/4) | 4 |
| a photo of a bowl | 100.0% (4/4) | 4 |
| a photo of a dog | 100.0% (4/4) | 4 |
| a photo of a handbag | 100.0% (4/4) | 4 |
| a photo of a stop sign | 100.0% (4/4) | 4 |
| a photo of a donut | 100.0% (4/4) | 4 |
| a photo of a pizza | 100.0% (4/4) | 4 |
| a photo of a sheep | 100.0% (4/4) | 4 |
| a photo of a teddy bear | 100.0% (4/4) | 4 |
| a photo of a fire hydrant | 100.0% (4/4) | 4 |
| a photo of a vase | 100.0% (4/4) | 4 |
| a photo of a banana | 100.0% (4/4) | 4 |
| a photo of a toothbrush | 100.0% (4/4) | 4 |
| a photo of a tv remote | 100.0% (4/4) | 4 |
| a photo of an apple | 100.0% (4/4) | 4 |
| a photo of an airplane | 100.0% (4/4) | 4 |
| a photo of a bus | 100.0% (4/4) | 4 |
| a photo of a tennis racket | 100.0% (4/4) | 4 |
| a photo of a knife | 100.0% (4/4) | 4 |
| a photo of a dining table | 100.0% (4/4) | 4 |
| a photo of a hot dog | 100.0% (4/4) | 4 |
| a photo of a boat | 100.0% (4/4) | 4 |
| a photo of a sports ball | 100.0% (4/4) | 4 |
| a photo of a baseball glove | 100.0% (4/4) | 4 |
| a photo of a bear | 100.0% (4/4) | 4 |
| a photo of a hair drier | 100.0% (4/4) | 4 |
| a photo of a kite | 100.0% (4/4) | 4 |
| a photo of a giraffe | 100.0% (4/4) | 4 |
| a photo of a bench and a sports ball | 100.0% (4/4) | 4 |
| a photo of a cake | 100.0% (4/4) | 4 |
| a photo of a horse | 100.0% (4/4) | 4 |
| a photo of a wine glass | 100.0% (4/4) | 4 |
| a photo of a truck | 100.0% (4/4) | 4 |
| a photo of a cat | 100.0% (4/4) | 4 |
| a photo of a toaster and an oven | 100.0% (4/4) | 4 |
| a photo of an umbrella | 100.0% (4/4) | 4 |
| a photo of a tennis racket and a wine glass | 100.0% (4/4) | 4 |
| a photo of a broccoli and a vase | 100.0% (4/4) | 4 |
| a photo of a hair drier and a bear | 100.0% (4/4) | 4 |
| a photo of a fork and a knife | 100.0% (4/4) | 4 |
| a photo of a couch and a horse | 100.0% (4/4) | 4 |
| a photo of a hair drier and a cake | 100.0% (4/4) | 4 |
| a photo of a knife and a zebra | 100.0% (4/4) | 4 |
| a photo of a horse and a giraffe | 100.0% (4/4) | 4 |
| a photo of a couch and a wine glass | 100.0% (4/4) | 4 |
| a photo of a horse and a computer keyboard | 100.0% (4/4) | 4 |
| a photo of a book and a laptop | 100.0% (4/4) | 4 |
| a photo of a dining table and a bear | 100.0% (4/4) | 4 |
| a photo of a frisbee and a couch | 100.0% (4/4) | 4 |
| a photo of a cake and a zebra | 100.0% (4/4) | 4 |
| a photo of a couch and a snowboard | 100.0% (4/4) | 4 |
| a photo of a fork and a baseball glove | 100.0% (4/4) | 4 |
| a photo of a bus and a baseball glove | 100.0% (4/4) | 4 |
| a photo of a person and a stop sign | 100.0% (4/4) | 4 |
| a photo of a bottle and a refrigerator | 100.0% (4/4) | 4 |
| a photo of a potted plant and a backpack | 100.0% (4/4) | 4 |
| a photo of a skateboard and a cake | 100.0% (4/4) | 4 |
| a photo of a broccoli and a parking meter | 100.0% (4/4) | 4 |
| a photo of a zebra and a bed | 100.0% (4/4) | 4 |
| a photo of an oven and a bed | 100.0% (4/4) | 4 |
| a photo of a baseball bat and a fork | 100.0% (4/4) | 4 |
| a photo of a vase and a spoon | 100.0% (4/4) | 4 |
| a photo of a skateboard and a sink | 100.0% (4/4) | 4 |
| a photo of a pizza and a bench | 100.0% (4/4) | 4 |
| a photo of a tennis racket and a bird | 100.0% (4/4) | 4 |
| a photo of a wine glass and a bear | 100.0% (2/2) | 2 |
| a photo of a stop sign and a fork | 100.0% (4/4) | 4 |
| a photo of a potted plant and a boat | 100.0% (4/4) | 4 |
| a photo of a tv and a cell phone | 100.0% (4/4) | 4 |
| a photo of a tie and a broccoli | 100.0% (4/4) | 4 |
| a photo of a potted plant and a donut | 100.0% (4/4) | 4 |
| a photo of a person and a sink | 100.0% (4/4) | 4 |
| a photo of an apple and a toothbrush | 100.0% (4/4) | 4 |
| a photo of a carrot and a couch | 100.0% (4/4) | 4 |
| a photo of a fire hydrant and a train | 100.0% (4/4) | 4 |
| a photo of a baseball glove and a carrot | 100.0% (4/4) | 4 |
| a photo of a cake and a stop sign | 100.0% (4/4) | 4 |
| a photo of a car and a computer mouse | 100.0% (4/4) | 4 |
| a photo of a suitcase and a dining table | 100.0% (4/4) | 4 |
| a photo of a person and a traffic light | 100.0% (4/4) | 4 |
| a photo of a cell phone and a horse | 100.0% (4/4) | 4 |
| a photo of four handbags | 100.0% (4/4) | 4 |
| a photo of two bears | 100.0% (4/4) | 4 |
| a photo of three persons | 100.0% (4/4) | 4 |
| a photo of three tennis rackets | 100.0% (4/4) | 4 |
| a photo of four bowls | 100.0% (4/4) | 4 |
| a photo of three cups | 100.0% (4/4) | 4 |
| a photo of two ovens | 100.0% (4/4) | 4 |
| a photo of two toilets | 100.0% (4/4) | 4 |
| a photo of three buses | 100.0% (4/4) | 4 |
| a photo of three snowboards | 100.0% (4/4) | 4 |
| a photo of two snowboards | 100.0% (4/4) | 4 |
| a photo of four dogs | 100.0% (4/4) | 4 |
| a photo of two sheeps | 100.0% (4/4) | 4 |
| a photo of three zebras | 100.0% (4/4) | 4 |
| a photo of three kites | 100.0% (4/4) | 4 |
| a photo of three cell phones | 100.0% (4/4) | 4 |
| a photo of four baseball gloves | 100.0% (4/4) | 4 |
| a photo of two beds | 100.0% (4/4) | 4 |
| a photo of two tv remotes | 100.0% (4/4) | 4 |
| a photo of three fire hydrants | 100.0% (4/4) | 4 |
| a photo of four giraffes | 100.0% (4/4) | 4 |
| a photo of two vases | 100.0% (4/4) | 4 |
| a photo of four donuts | 100.0% (4/4) | 4 |
| a photo of four chairs | 100.0% (4/4) | 4 |
| a photo of two fire hydrants | 100.0% (4/4) | 4 |
| a photo of three giraffes | 100.0% (4/4) | 4 |
| a photo of four tvs | 100.0% (4/4) | 4 |
| a photo of three wine glasses | 100.0% (4/4) | 4 |
| a photo of three trucks | 100.0% (4/4) | 4 |
| a photo of two trucks | 100.0% (4/4) | 4 |
| a photo of four clocks | 100.0% (4/4) | 4 |
| a photo of four knifes | 100.0% (4/4) | 4 |
| a photo of four zebras | 100.0% (4/4) | 4 |
| a photo of two teddy bears | 100.0% (4/4) | 4 |
| a photo of three birds | 100.0% (4/4) | 4 |
| a photo of four microwaves | 100.0% (4/4) | 4 |
| a photo of two hair driers | 100.0% (4/4) | 4 |
| a photo of three laptops | 100.0% (4/4) | 4 |
| a photo of three cows | 100.0% (4/4) | 4 |
| a photo of a blue fire hydrant | 100.0% (4/4) | 4 |
| a photo of a pink car | 100.0% (4/4) | 4 |
| a photo of a purple cup | 100.0% (4/4) | 4 |
| a photo of a blue cow | 100.0% (4/4) | 4 |
| a photo of a fork and a book | 100.0% (4/4) | 4 |
| a photo of a scissors and a bowl | 100.0% (4/4) | 4 |
| a photo of a laptop and a carrot | 100.0% (4/4) | 4 |
| a photo of a stop sign and a bottle | 100.0% (4/4) | 4 |
| a photo of a microwave and a truck | 100.0% (4/4) | 4 |
| a photo of a person and a bear | 100.0% (4/4) | 4 |
| a photo of a frisbee and a cell phone | 100.0% (4/4) | 4 |
| a photo of a parking meter and a teddy bear | 100.0% (4/4) | 4 |
| a photo of a tennis racket and a bicycle | 100.0% (4/4) | 4 |
| a photo of a stop sign and a motorcycle | 100.0% (4/4) | 4 |
| a photo of a fire hydrant and a tennis racket | 100.0% (4/4) | 4 |
| a photo of a scissors and a sandwich | 100.0% (4/4) | 4 |
| a photo of a pizza and a book | 100.0% (4/4) | 4 |
| a photo of a giraffe and a computer mouse | 100.0% (4/4) | 4 |
| a photo of a stop sign and a toaster | 100.0% (4/4) | 4 |
| a photo of a computer mouse and a zebra | 100.0% (4/4) | 4 |
| a photo of a chair and a bench | 100.0% (4/4) | 4 |
| a photo of a tv and a carrot | 100.0% (4/4) | 4 |
| a photo of a surfboard and a suitcase | 100.0% (4/4) | 4 |
| a photo of a computer keyboard and a laptop | 100.0% (4/4) | 4 |
| a photo of a computer keyboard and a microwave | 100.0% (4/4) | 4 |
| a photo of a scissors and a bird | 100.0% (4/4) | 4 |
| a photo of a person and a snowboard | 100.0% (4/4) | 4 |
| a photo of a cow and a horse | 100.0% (4/4) | 4 |
| a photo of a handbag and a refrigerator | 100.0% (4/4) | 4 |
| a photo of a chair and a laptop | 100.0% (4/4) | 4 |
| a photo of a toothbrush and a bench | 100.0% (4/4) | 4 |
| a photo of a book and a baseball bat | 100.0% (4/4) | 4 |
| a photo of a horse and a train | 100.0% (4/4) | 4 |
| a photo of a bench and a vase | 100.0% (4/4) | 4 |
| a photo of a traffic light and a backpack | 100.0% (4/4) | 4 |
| a photo of a sports ball and a cow | 100.0% (4/4) | 4 |
| a photo of a computer mouse and a spoon | 100.0% (4/4) | 4 |
| a photo of a tv and a bicycle | 100.0% (4/4) | 4 |
| a photo of a bench and a snowboard | 100.0% (4/4) | 4 |
| a photo of a toothbrush and a toilet | 100.0% (4/4) | 4 |
| a photo of a person and an apple | 100.0% (4/4) | 4 |
| a photo of a sink and a sports ball | 100.0% (4/4) | 4 |
| a photo of a stop sign and a dog | 100.0% (4/4) | 4 |
| a photo of a knife and a stop sign | 100.0% (4/4) | 4 |
| a photo of a wine glass and a handbag | 100.0% (4/4) | 4 |
| a photo of a bowl and a skis | 100.0% (4/4) | 4 |
| a photo of a frisbee and an apple | 100.0% (4/4) | 4 |
| a photo of a computer keyboard and a cell phone | 100.0% (4/4) | 4 |
| a photo of a blue umbrella | 100.0% (4/4) | 4 |
| a photo of a blue elephant | 100.0% (4/4) | 4 |
| a photo of a yellow elephant | 100.0% (4/4) | 4 |
| a photo of a purple suitcase | 100.0% (4/4) | 4 |
| a photo of a purple hair drier | 100.0% (4/4) | 4 |
| a photo of a purple elephant | 100.0% (4/4) | 4 |
| a photo of a green microwave | 100.0% (4/4) | 4 |
| a photo of a red zebra | 100.0% (4/4) | 4 |
| a photo of a red apple | 100.0% (4/4) | 4 |
| a photo of a yellow tv remote | 100.0% (4/4) | 4 |
| a photo of a blue toilet | 100.0% (4/4) | 4 |
| a photo of an orange orange | 100.0% (4/4) | 4 |
| a photo of a black donut | 100.0% (4/4) | 4 |
| a photo of a red vase | 100.0% (4/4) | 4 |
| a photo of a purple pizza | 100.0% (4/4) | 4 |
| a photo of a pink skateboard | 100.0% (4/4) | 4 |
| a photo of a green skateboard | 100.0% (4/4) | 4 |
| a photo of a purple bear | 100.0% (4/4) | 4 |
| a photo of a brown chair | 100.0% (4/4) | 4 |
| a photo of an orange cow | 100.0% (4/4) | 4 |
| a photo of a green couch | 100.0% (4/4) | 4 |
| a photo of a yellow airplane | 100.0% (4/4) | 4 |
| a photo of an orange tv | 100.0% (4/4) | 4 |
| a photo of a pink cell phone | 100.0% (4/4) | 4 |
| a photo of a green surfboard | 100.0% (4/4) | 4 |
| a photo of a white fire hydrant | 100.0% (4/4) | 4 |
| a photo of a black bicycle | 100.0% (4/4) | 4 |
| a photo of a black dining table | 100.0% (4/4) | 4 |
| a photo of a purple potted plant | 100.0% (4/4) | 4 |
| a photo of a purple backpack | 100.0% (4/4) | 4 |
| a photo of a yellow train | 100.0% (4/4) | 4 |
| a photo of a brown bear | 100.0% (4/4) | 4 |
| a photo of an orange laptop | 100.0% (4/4) | 4 |
| a photo of a yellow parking meter | 100.0% (4/4) | 4 |
| a photo of a green traffic light | 100.0% (4/4) | 4 |
| a photo of a blue tv | 100.0% (4/4) | 4 |
| a photo of a purple scissors | 100.0% (4/4) | 4 |
| a photo of a brown toaster | 100.0% (4/4) | 4 |
| a photo of a green clock | 100.0% (4/4) | 4 |
| a photo of a yellow oven | 100.0% (4/4) | 4 |
| a photo of a green vase | 100.0% (4/4) | 4 |
| a photo of a black teddy bear | 100.0% (4/4) | 4 |
| a photo of a red scissors | 100.0% (4/4) | 4 |
| a photo of a white teddy bear | 100.0% (4/4) | 4 |
| a photo of a black skis | 100.0% (4/4) | 4 |
| a photo of a blue dining table | 100.0% (4/4) | 4 |
| a photo of a black refrigerator | 100.0% (4/4) | 4 |
| a photo of a white dog | 100.0% (4/4) | 4 |
| a photo of an orange scissors | 100.0% (4/4) | 4 |
| a photo of a red cell phone | 100.0% (4/4) | 4 |
| a photo of a blue clock | 100.0% (4/4) | 4 |
| a photo of a green motorcycle | 100.0% (4/4) | 4 |
| a photo of a pink stop sign | 100.0% (4/4) | 4 |
| a photo of a black vase | 100.0% (4/4) | 4 |
| a photo of a black backpack | 100.0% (4/4) | 4 |
| a photo of a red car | 100.0% (4/4) | 4 |
| a photo of a green computer mouse | 100.0% (4/4) | 4 |
| a photo of a red backpack | 100.0% (4/4) | 4 |
| a photo of a green bus | 100.0% (4/4) | 4 |
| a photo of an orange toaster | 100.0% (4/4) | 4 |
| a photo of a yellow fork | 100.0% (4/4) | 4 |
| a photo of a pink parking meter | 100.0% (4/4) | 4 |
| a photo of an orange computer mouse | 100.0% (4/4) | 4 |
| a photo of a red cake | 100.0% (4/4) | 4 |
| a photo of a dog right of a teddy bear | 100.0% (4/4) | 4 |
| a photo of a couch below a cup | 100.0% (4/4) | 4 |
| a photo of a train above a potted plant | 100.0% (4/4) | 4 |
| a photo of a baseball glove below an umbrella | 100.0% (4/4) | 4 |
| a photo of a bear above a clock | 100.0% (4/4) | 4 |
| a photo of a tennis racket right of a spoon | 100.0% (4/4) | 4 |
| a photo of a carrot left of an orange | 100.0% (4/4) | 4 |
| a photo of a toaster below a traffic light | 100.0% (4/4) | 4 |
| a photo of a skis right of a zebra | 100.0% (4/4) | 4 |
| a photo of a stop sign above a chair | 100.0% (4/4) | 4 |
| a photo of a stop sign above a parking meter | 100.0% (4/4) | 4 |
| a photo of a pizza below a computer keyboard | 100.0% (4/4) | 4 |
| a photo of a zebra right of a parking meter | 100.0% (4/4) | 4 |
| a photo of a chair left of a zebra | 100.0% (4/4) | 4 |
| a photo of a cow below an airplane | 100.0% (4/4) | 4 |
| a photo of a zebra below a broccoli | 100.0% (4/4) | 4 |
| a photo of a tv above a baseball bat | 100.0% (4/4) | 4 |
| a photo of a baseball glove right of a bear | 100.0% (4/4) | 4 |
| a photo of a zebra left of an elephant | 100.0% (4/4) | 4 |
| a photo of a frisbee above a truck | 100.0% (4/4) | 4 |
| a photo of a bus above a boat | 100.0% (4/4) | 4 |
| a photo of a horse right of a broccoli | 100.0% (4/4) | 4 |
| a photo of a frisbee below a horse | 100.0% (4/4) | 4 |
| a photo of a broccoli above a bottle | 100.0% (4/4) | 4 |
| a photo of a train below an airplane | 100.0% (4/4) | 4 |
| a photo of a clock below a tv | 100.0% (4/4) | 4 |
| a photo of a sandwich below a knife | 100.0% (4/4) | 4 |
| a photo of a couch below a vase | 100.0% (4/4) | 4 |
| a photo of a donut below a cat | 100.0% (4/4) | 4 |
| a photo of a couch left of a toaster | 100.0% (4/4) | 4 |
| a photo of a purple parking meter and a red laptop | 100.0% (4/4) | 4 |
| a photo of a yellow skateboard and an orange computer mouse | 100.0% (4/4) | 4 |
| a photo of a pink oven and a green motorcycle | 100.0% (4/4) | 4 |
| a photo of a red train and a purple bear | 100.0% (4/4) | 4 |
| a photo of a blue cell phone and a green apple | 100.0% (4/4) | 4 |
| a photo of a blue clock and a white cup | 100.0% (4/4) | 4 |
| a photo of a red umbrella and a blue couch | 100.0% (4/4) | 4 |
| a photo of a pink tv remote and a blue airplane | 100.0% (4/4) | 4 |
| a photo of an orange truck and a pink sink | 100.0% (4/4) | 4 |
| a photo of a green couch and an orange umbrella | 100.0% (4/4) | 4 |
| a photo of a yellow bowl and a white baseball glove | 100.0% (4/4) | 4 |
| a photo of a yellow dining table and a pink dog | 100.0% (4/4) | 4 |
| a photo of a red cake and a purple chair | 100.0% (4/4) | 4 |
| a photo of a blue tie and a pink dining table | 100.0% (4/4) | 4 |
| a photo of an orange handbag and a red car | 100.0% (4/4) | 4 |
| a photo of a yellow car and an orange toothbrush | 100.0% (4/4) | 4 |
| a photo of a green suitcase and a blue boat | 100.0% (4/4) | 4 |
| a photo of a green surfboard and an orange oven | 100.0% (4/4) | 4 |
| a photo of a yellow parking meter and a pink refrigerator | 100.0% (4/4) | 4 |
| a photo of a brown computer mouse and a purple bottle | 100.0% (4/4) | 4 |
| a photo of an orange tennis racket and a yellow sports ball | 100.0% (4/4) | 4 |
| a photo of a red umbrella and a green cow | 100.0% (4/4) | 4 |
| a photo of a purple computer keyboard and a red chair | 100.0% (4/4) | 4 |
| a photo of a green cup and a yellow bowl | 100.0% (4/4) | 4 |
| a photo of a green tennis racket and a black dog | 100.0% (4/4) | 4 |
| a photo of an orange motorcycle and a pink donut | 100.0% (4/4) | 4 |
| a photo of a yellow bird and a black motorcycle | 100.0% (4/4) | 4 |
| a photo of a red cup and a pink handbag | 100.0% (4/4) | 4 |
| a photo of a blue pizza and a yellow baseball glove | 100.0% (4/4) | 4 |

## Recommendations

- Model shows good performance with room for improvement
- Recommend detailed analysis of errors in weak categories
- Consider prompt optimization for problematic cases

## Technical Details

- **Evaluation Framework:** GenEval
- **Object Detection:** mask2former_swin-s-p4-w7-224_lsj_8x2_50e_coco
- **CLIP Model:** ViT-L-14
- **Detection Threshold:** 0.3 (0.9 for counting)
- **Images per Prompt:** 4

---
*Report generated automatically based on GenEval evaluation results*