# Relatório Legível de Auditoria de Qualidade (QualityGuard)

Este documento apresenta a leitura humana dos resultados da auditoria de controlo de qualidade realizada pelo `QualityGuardAgent` (`deepseek-v4-pro` com modo pensamento) sobre a codificação netnográfica.

---

## 1. Sumário Executivo da Auditoria

* **Data da Auditoria:** 2026-07-08 18:09:34
* **Universo Total de Análises:** 1443 posts
* **Tamanho da Amostra Auditada:** 288 posts (20.0%)
* **Score Médio de Consistência Global:** **`88.38%`** (Limiar mínimo de aprovação: 70.0%)
* **Classificação Final:** **APROVADO**
* **Auditorias com Alertas/Pontuação Baixa:** 56

### Taxa de Aprovação por Critério Teórico
* **Existência Literal da Evidência:** `72.3%` de conformidade (evidência existe no texto)
* **Consistência Conceptual DART:** `85.1%` de conformidade teórica
* **Fundamentação Válida do Risco:** `98.0%` de lógica de risco consistente
* **Coerência de Metadados e QIs:** `98.0%` de conformidade de metadados

---

## 2. Auditorias com Alerta ou Falha Registada

| ID do Post | Score | Motivo / Justificação da Auditoria |
| :--- | :---: | :--- |
| `3000013_19863116` | **65** | A evidência literal para a dimensão 'risco' contém a frase 'The amount of botting is unacceptable', que não está presente no post original. O corpo do post apenas menciona 'It’s become a huge issue. You can see it in game and out.', sem a primeira parte. Além disso, a análise de 'diálogo' é inconsistente conceitualmente, pois classifica como diálogo presente uma interação entre jogadores, enquanto o framework DART pressupõe comunicação de dupla via entre empresa e consumidores; a própria análise admite que não é com os desenvolvedores, o que enfraquece a validade da classificação. O score de risco 5 é justificável com base no tom geral do post, mas a fundamentação referencia evidência não literal, o que reduz a robustez. Os metadados estão corretos. |
| `514029_2895732` | **75** | As evidências literais para as dimensões Acesso e Risco referem-se a frases que não constam no corpo do post original (apenas no título). As interpretações conceituais e a fundamentação do risco estão corretas, assim como a coerência dos metadados. |
| `3000008_25930019` | **80** | A evidência literal para a dimensão 'acesso' é apresentada como 'People cant even afford raid consumes. the people buying gold can afford things'. Esta frase exata não consta de forma literal no post original, que tem: 'People cant even afford raid consumes because the market went right to whitemane era prices.' seguido de 'Incorrect, the people buying gold can afford things'. A concatenação e remoção de parte da frase original quebram a literalidade. Todas as outras dimensões apresentam evidências literais válidas e o enquadramento teórico, a fundamentação do risco e os metadados estão corretos e consistentes. |
| `512885_2886699` | **80** | A evidencia_literal fornecida 'Shuttle Smart-bombing Is Anti-Gameplay, Not PvP ... That is way too much effort for today’s player.' não existe literalmente no corpo do post original, pois o corpo contém apenas a frase final e a citação de outro utilizador, mas não o título. A concatenação com '...' e a inclusão do título tornam o excerto não correspondente a qualquer substring do corpo, violando o requisito de evidência literal. As análises concetuais, a fundamentação do score de risco e a coerência dos metadados estão corretas. |
| `514029_2896810` | **75** | A evidência literal para a dimensão 'risco' ('Game-breaking lack of enforcement against input broadcasting / multi-input automation') provém do título do post original, mas não está presente no corpo do texto, violando o requisito de extração literal do corpo. As demais evidências ('player base that still remains seems to have shifted to this type of gameplay' e 'was unforeseeable at the time? Don’t know, just asking.') são literais do corpo. As interpretações conceituais estão alinhadas com o framework DART, a fundamentação do score de risco é coerente e os metadados estão consistentes com o post original. |
| `509843_2862526` | **85** | A evidência literal está corretamente vazia porque não há frases que suportem as dimensões. A fundamentação do risco percebido está lógica. Metadados coerentes. No entanto, há uma inconsistência conceptual: a 'dimensão dominante' é definida como 'dialogo', mas essa dimensão foi avaliada como não presente, o que contradiz a teoria DART. |
| `511200_2873992` | **20** | Erro crítico: as evidências literais para Risco e Transparência foram extraídas do título do post ('Why is CCP punishing real players while looking the other way on botting?'), mas o corpo do post não contém essas frases. O corpo trata exclusivamente de um debate acalorado sobre argumentação, sem qualquer menção a bots, punições ou transparência da CCP. Portanto, 'evidencia_literal_existe' é falso para essas dimensões. A consistência conceitual falha porque Risco e Transparência são mapeados incorretamente a partir do título, não do conteúdo. A fundamentação do score de risco (4) baseia-se nessa evidência inexistente no corpo, invalidando-a. A presença errática dessas dimensões torna o mapeamento das QIs (QI3, QI4) inconsistente com o conteúdo real. Apenas Diálogo está corretamente identificado. A auditoria geral é negativa. |
| `509972_2863247` | **75** | A auditoria revelou que a evidência literal para a dimensão ‘risco’ não está presente de forma exacta no post original. O texto do post contém ‘their chars teleported to Solitude after given a fair warning’, enquanto a análise cita ‘chars teleported to Solitude after given a fair warning’ (omissão do pronome ‘their’). Este pequeno desvio invalida a correspondência literal exigida. As restantes dimensões apresentam evidências literais válidas. Conceptual, a análise está correcta e alinhada com o framework DART. A fundamentação do score de risco (3) é coerente com o conteúdo. Os metadados (jogo, ID, QIs) são consistentes. Por isso, atribui-se uma pontuação de 75, penalizando apenas a não literalidade da evidência de risco. |
| `11pmlty_5` | **85** | As evidências literais para 'acesso' (falta 'at,') e 'transparência' (falta '...') não são transcrições exatas do post original, violando o critério de literalidade. As interpretações conceituais, a fundamentação do score de risco (5) e os metadados estão corretos. |
| `3000003_28811596` | **40** | A evidência literal corresponde exatamente ao corpo do post. O score de risco percebido (1) está bem justificado pela ausência de menção a riscos. Os metadados (jogo, ID, mapeamento de QIs) são coerentes. Contudo, a classificação do Diálogo como 'presente' é conceitualmente inconsistente com as definições do framework DART: o post é uma sugestão isolada, sem evidência de interatividade, escuta ou comunicação bidirecional exigida para caracterizar diálogo. A interpretação de uma proposta unilateral como 'diálogo iniciado pelo jogador' distorce o conceito, comprometendo a validade da análise. Por esse erro principal, a pontuação da auditoria é reduzida. |
| `504046_2821673` | **80** | As evidências literais listadas estão presentes no texto original. A conceitualização do Diálogo é inconsistente: uma única pergunta sem resposta visível não caracteriza dialogo autêntico segundo o modelo DART (o próprio analista admite falta de escuta ativa e negociação profunda). A fundamentação do risco está lógica e bem justificada. Metadados são coerentes. |
| `511200_2873732` | **50** | As evidências literais para as dimensões 'risco' ('Why is CCP punishing real players while looking the other way on botting?') e 'transparência' ('looking the other way on botting') foram extraídas do título do post, não do seu corpo, conforme exigido pelo critério. O corpo não contém essas frases. As evidências para 'diálogo' e 'acesso' estão corretas. As interpretações conceituais, a fundamentação do score de risco e os metadados do jogo e QIs são consistentes. |
| `2059924_26285238` | **85** | As evidências literais listadas para Diálogo, Acesso e Risco estão presentes no post. Para Transparência, a ausência está corretamente indicada. A fundamentação do score de risco é lógica e consistente. Os metadados (jogo, ID, QIs) são coerentes. No entanto, a consistência conceitual do Acesso é frágil: a mera observação de bots não constitui 'acesso' no sentido clássico do DART, que se refere ao acesso a ferramentas, informação ou processos para co-criação. A interpretação de Diálogo é aceitável, mas o enquadramento de Acesso diverge. Por isso, a análise não é totalmente consistente conceitualmente, justificando a pontuação atribuída. |
| `1rvfe34_3` | **75** | As evidências literais listadas para as dimensões de Risco e Transparência ('Got permabanned for RMT out of nowhere, just paid for 2 years of Omega' e 'Got permabanned for RMT out of nowhere') constam apenas no título do post, e não no corpo ('Corpo: My wallet has like 20 million ISK...'). A exigência é que as frases estejam literalmente no corpo do post original, o que não se verifica. A consistência conceitual do DART, a fundamentação do score de risco (5) e a coerência dos metadados estão corretas. Por este motivo, a análise perde 25 pontos. |
| `511200_2873986` | **80** | A evidência literal para a dimensão 'acesso' é uma concatenação de duas frases não contíguas no post original ('I use tools to check my grammar and make sure I’m being clear.' e 'BTW I use translator + grammarly.'), não correspondendo a uma citação literal exata. As demais dimensões apresentam evidências presentes. A análise conceitual e os metadados estão corretos. |
| `3000006_27244798` | **65** | A evidência literal existe para as dimensões 'acesso' e 'risco', e os metadados estão coerentes. A fundamentação do score de risco é válida e bem justificada. No entanto, a dimensão 'acesso' foi aplicada de forma inconsistente com o conceito original do framework DART, que diz respeito ao acesso a informação, ferramentas e interfaces para cocriação, e não à disponibilidade de recursos do jogo. O post não aborda acesso a ferramentas de cocriação, logo a presença marcada como 'true' para esta dimensão representa um erro conceitual significativo. |
| `3000000_22981406` | **40** | A evidência literal para a dimensão 'Risco' não é uma citação contígua do post; combina duas frases separadas com reticências, não constituindo um excerto verbatim único. Conceitualmente, a análise interpreta 'Diálogo' como comunicação entre jogadores, quando o framework DART pressupõe interação humano-IA ou humano-desenvolvedor; o 'Risco' é enquadrado como risco económico do jogo, e não como risco percebido no uso de funcionalidades com IA. Estes desvios violam as definições clássicas. A pontuação de risco (2) está internamente justificada com base no texto, e os metadados são coerentes. Por estas razões, a análise é parcialmente válida mas falha em critérios fundamentais. |
| `3000008_25925089` | **75** | Todas as evidências literais citadas existem exatamente no post original. A fundamentação do score de risco 3 está lógica e bem justificada, e os metadados (jogo, ID, questões de investigação) são coerentes. No entanto, a dimensão 'Acesso' é conceptualmente inconsistente: o uso de GDKPs como ferramenta de equalização económica não se alinha com a definição clássica de Acesso no modelo DART, que se refere ao fornecimento de acesso a informações, dados ou ferramentas pela empresa para cocriação de valor. Aqui, trata-se de um sistema criado por jogadores, não oferecido pela Blizzard, o que invalida o enquadramento teórico dessa dimensão. |
| `511200_2872836` | **30** | As frases de evidência literal listadas em 'Diálogo', 'Acesso', 'Risco' e 'Transparência' não se encontram no corpo do post original. Todas as alegações de evidência baseiam‑se no título ou em combinações que incluem o título, enquanto a auditoria exige presença literal no corpo da mensagem. Isto compromete a validade da análise. Apesar de a consistência teórica das definições DART estar correta e a fundamentação do risco percebido fazer sentido considerando o texto completo (título + corpo), a ausência total de evidência literal de suporte é uma falha crítica que reduz substancialmente a pontuação. |
| `513682_2897017` | **80** | A evidência literal para as dimensões 'acesso' e 'risco' é apresentada como concatenações de fragmentos ('input broadcasting programs ... alt-tab / eve-o / windows cascade clicking' e 'Add a hard-coded client switching delay ... to motivate players who are not cheating to cheat? ... This just smell as another stupid ganking nerf') que não existem como frases únicas e literais no post, embora os elementos individuais estejam presentes. As definições conceituais das dimensões DART estão corretas. A fundamentação do score de risco está alinhada com o conteúdo e é lógica. Os metadados estão coerentes. A qualidade geral da análise é boa, mas a não literalidade exata no 'evidencia_literal' reduz ligeiramente a pontuação. |
| `513682_2892720` | **60** | O critério de evidência literal não é cumprido: a frase listada para a dimensão Acesso ('Input broadcasters or similar programs!') encontra-se no título e não no corpo do post original, violando a exigência de que a evidência deve existir literalmente no corpo. A consistência concetual é fraca: a dimensão Diálogo é tida como presente, mas o post não evidencia interação dialógica genuína — é sobretudo uma afirmação pessoal sobre perícia, o que não se enquadra na definição clássica de diálogo interativo. O score de risco (3) e a sua fundamentação são válidos e estão em linha com o conteúdo. Os metadados (jogo, ID e mapeamento das QI) estão coerentes. |
| `3000012_25620442` | **75** | A evidência literal da dimensão Acesso ('players that take short cuts. GDKPers that dont have the time to farm gold') não é uma substring exata do post original, que contém 'players that take short cuts. GDKPers that “dont have the time to farm gold”' (com aspas). A evidência literal da dimensão Risco inclui 'bots still wrecked the AH', que não aparece textualmente; o post diz 'they still wrecked the AH' referindo-se a bots indiretamente. Apesar disso, as interpretações conceituais DART estão corretas, a fundamentação do score de risco (5) é lógica e os metadados são coerentes. Por essa imprecisão nas evidências literais, a análise perde pontos, mas mantém qualidade geral. |
| `1t81ix0_6` | **70** | A evidência literal citada ('pretty easy to see how it works without breaking any rules') existe exatamente no post. A fundamentação do risco percebido (4/5) é lógica e coerente com o contexto de EVE Online. Os metadados estão coerentes. Contudo, a dimensão 'Diálogo' foi mal enquadrada conceitualmente: segundo as definições clássicas de DART, diálogo exige interatividade e bilateralidade, enquanto o post é um compartilhamento unidirecional de informação entre jogadores, não configurando um ato de diálogo com a empresa ou mesmo um diálogo estruturado entre pares. A interpretação teórica forçada compromete a consistência conceitual. |
| `xaonz7_10` | **85** | A evidência literal na dimensão Risco apresenta uma citação composta por duas frases não contíguas no texto original ('Botting is a pretty serious issue, but treating players as bots is also a pretty serious issue. if it does then the bots are going to win based on the law of averages.'), o que viola o critério de existência de uma única sequência literal contínua. As demais evidências são literais, e as interpretações conceituais, score de risco e metadados estão corretos. Dedução de 15 pontos por essa não conformidade. |
| `509129_2862258` | **90** | A evidência literal para Transparência ('Team Security [ID_ANONYMIZED] Bans ... 4k in Feb, 6k in March. 8k in April maybe??') mistura título e corpo com reticências não presentes no post original, não constituindo uma citação exata do corpo. As restantes evidências, a interpretação conceitual DART, a fundamentação do score de risco e a coerência dos metadados estão corretas. |
| `509129_2863223` | **60** | A evidência literal está correta: as frases indicadas existem no post. A coerência de metadados é válida. A fundamentação do score de risco é lógica. No entanto, a consistência conceitual falha nos seguintes pontos: (1) Diálogo: no quadro DART clássico, diálogo refere-se à interação direta e interessada entre empresa e consumidor, não a um debate indireto entre jogadores sobre a empresa; a análise interpreta erroneamente uma discussão entre pares como diálogo DART. (2) Risco: o conceito de risco em DART diz respeito ao risco partilhado na cocriação de valor, não ao risco genérico de integridade do jogo por bots. A análise equipara “risco de muitos bots” a risco DART, o que é um desvio conceitual. (3) Transparência: a análise afirma que a transparência está presente, mas na realidade o post evidencia uma assimetria de informação (a CCP sabe mais), o que configura falta de transparência. A atribuição de 'presente: true' e a interpretação subsequente não respeitam a definição clássica de transparência como informação simétrica e disponível. Pontos fortes: evidência literal correta, metadados coerentes e justificação do score de risco válida. |
| `1hs6hm3_10` | **90** | A análise está correta em todas as dimensões, com exceção da evidência literal para a dimensão Risco. A frase citada como 'evidencia_literal' não corresponde exatamente ao texto original: omite um 'so' ('so so far' no original vs. 'so far' na análise). Todos os outros aspetos (consistência conceitual, fundamentação do risco e coerência de metadados) estão válidos. |
| `xaonz7_2` | **40** | A evidência literal de 'risco' e 'transparência' não corresponde a frases exatas do post: a de 'risco' usa reticências para omitir 'I said this in other post but botting in EVE is like crypto mining.' e a de 'transparência' omite 'they are so deep in shit', quebrando a literalidade. A conceptualização de Acesso está equivocada, pois no framework DART o acesso refere-se a recursos disponibilizados pela empresa para cocriação, e não a mercados ilícitos como o RMT. Os scores de risco e metadados estão corretos e bem justificados. |
| `1uq9f5i_4` | **65** | A evidência literal para a dimensão Acesso ('Hackers are engineering botting in Darktide') não está no corpo do post, apenas no título. A evidência para Risco ('If Botting comes for Darktide... This is just the current beta😞😕') combina corpo e título, sendo que a parte 'This is just the current beta😞😕' também não consta do corpo. Apenas a evidência de Diálogo é literalmente do corpo. Isso viola o critério de existência literal no corpo do post original. As demais análises conceituais, de risco e metadados estão corretas. |
| `3000007_29299356` | **90** | A evidência literal para a dimensão 'diálogo' contém reticências e omite parte da frase, não sendo uma citação exata do post original. As demais evidências literais são válidas. O enquadramento teórico, a fundamentação do risco e a coerência dos metadados estão corretos. |

*(Exibindo as primeiras 30 de 56 ocorrências com alertas/erros)*


---

## 3. Registo Detalhado da Amostra Auditada

### Post Auditado #1: `3000012_25620679` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A análise apresenta a frase exata do post como evidência literal para a dimensão Risco, e não lista evidências inexistentes. As definições das dimensões DART estão corretas e a interpretação teórica do Risco é consistente. A fundamentação do score de risco 3 está alinhada com o tom especulativo e a incerteza expressa no post. Os metadados (jogo, ID, QIs) são internamente coerentes e plausíveis.

---

### Post Auditado #2: `511102_2873005` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais citadas ('Tell me you don’t understand why ppl leave?...' e 'massmultiboxing is so incredible efficient...') aparecem exatamente no post original. A interpretação teórica de diálogo e risco está alinhada com as definições do framework DART, enquanto acesso e transparência estão ausentes, o que é correto. O score de risco 2 é bem fundamentado na postura do autor (minimização da ameaça, experiência TLA) e nos metadados (0 likes, trust level 2). Os metadados (jogo, ID, QIs mapeadas) são coerentes com o post e a análise.

---

### Post Auditado #3: `511200_2872766` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais ('CCP punishing real players while looking the other way on botting' e 'Fenris with silent R is thier new developer name') existem exatamente no post original. As interpretações conceituais de Diálogo, Acesso, Risco e Transparência estão alinhadas com as definições do framework DART. O score de risco 4 é coerente com o teor da queixa e a fundamentação menciona adequadamente o impacto da assimetria na aplicação de regras; o uso de likes e trust level como moderadores é aceitável. Os metadados (jogo, ID, mapeamento de QIs) mostram consistência total.

---

### Post Auditado #4: `1388935_18347883` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais citadas estão presentes textualmente no post original. A interpretação de Acesso, Risco e Transparência está alinhada com as definições clássicas do DART. O score de risco 5 é plenamente justificado pelo relato de ameaça existencial à economia e ausência de punição. Os metadados (jogo, ID, questões de investigação) são consistentes e adequados.

---

### Post Auditado #5: `510142_2865096` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais indicadas em cada dimensão DART existem de forma exata no post original (corpo ou título). As interpretações teóricas estão alinhadas com as definições clássicas de Diálogo, Acesso, Risco e Transparência. O score de risco 5 é bem fundamentado com base no sarcasmo, no tom de urgência e no nível de experiência do utilizador. Os metadados (jogo, ID, QIs) são coerentes e não apresentam inconsistências. Nenhum erro detetado.

---

### Post Auditado #6: `3000000_22977085` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Auditoria completa sem erros detectados: a evidência literal 'With bots no longer injecting raw gold back into the system as often, the economy of Whitemane is experiencing these effects.' consta exatamente no post original; a classificação das dimensões DART está conceitualmente correta (diálogo, acesso e transparência ausentes, risco presente com base na definição); o score de risco percebido 2 é justificado pela perceção positiva do jogador face à deflação e pelo baixo alarme; os metadados (jogo, ID, mapeamento das QIs) são coerentes com o conteúdo e o framework.

---

### Post Auditado #7: `3000011_23367215` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais citadas estão presentes no post original. As dimensões DART (Diálogo, Acesso, Risco, Transparência) foram interpretadas corretamente conforme as definições clássicas, com Risco e Transparência pertinentes ao conteúdo. O score de risco 3 está bem fundamentado, considerando o alerta moderado e a falta de endosso social (0 likes) do autor. Os metadados (jogo, ID) estão corretos e o mapeamento das questões de investigação (QI3, QI4, QI5) é coerente com a análise. Nenhum erro identificado.

---

### Post Auditado #8: `499582_2788469` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais estão presentes exatamente no post original. O enquadramento teórico das dimensões DART está correto: Diálogo e Acesso foram corretamente ausentes, Risco e Transparência corretamente presentes e alinhados com as definições clássicas. O score de risco 5 é bem fundamentado, refletindo a denúncia de cumplicidade estrutural da CCP. Metadados (jogo, ID, QIs mapeadas) são consistentes e não apresentam discrepâncias.

---

### Post Auditado #9: `513682_2892543` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais foram localizadas textualmente no post original. As interpretações teóricas das dimensões DART (Diálogo, Acesso, Risco, Transparência) seguem as definições clássicas de Prahalad & Ramaswamy (2004). A fundamentação para o score de risco 4 é lógica, baseada no conteúdo do post e nos metadados (trust level, edits). Os metadados (jogo, ID, trust, likes) e o mapeamento das questões de investigação (QI1 a QI5) são coerentes e abrangem todos os elementos relevantes. Análise de alta qualidade.

---

### Post Auditado #10: `504046_2821669` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A análise está correta em todos os critérios. A evidência literária do diálogo existe integralmente no post, as definições DART estão aplicadas consistentemente, o score de risco percebido (1) é justificado pela ausência de menção a riscos, e os metadados são coerentes com o post e o mapeamento das QIs. Não foram detetados erros.

---

### Post Auditado #11: `3000012_25620707` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Auditoria confirma qualidade da análise. Evidências literais citadas existem exatamente no post original. Conceitos DART aplicados corretamente: diálogo ausente (post unidirecional), acesso não mencionado, risco presente e bem fundamentado, transparência ausente. Score de risco 5 sustenta-se no tom de infestação inevitável e dano sistémico, coerente com o texto. Metadados (jogo, ID, QIs) consistentes. Sem erros detetados.

---

### Post Auditado #12: `3000013_19863116` — Score: **65/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **NÃO** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal para a dimensão 'risco' contém a frase 'The amount of botting is unacceptable', que não está presente no post original. O corpo do post apenas menciona 'It’s become a huge issue. You can see it in game and out.', sem a primeira parte. Além disso, a análise de 'diálogo' é inconsistente conceitualmente, pois classifica como diálogo presente uma interação entre jogadores, enquanto o framework DART pressupõe comunicação de dupla via entre empresa e consumidores; a própria análise admite que não é com os desenvolvedores, o que enfraquece a validade da classificação. O score de risco 5 é justificável com base no tom geral do post, mas a fundamentação referencia evidência não literal, o que reduz a robustez. Os metadados estão corretos.

---

### Post Auditado #13: `514029_2896861` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todos os critérios foram rigorosamente cumpridos: as evidências literais citadas para as dimensões 'acesso' e 'risco' constam exatamente no post original (título e corpo); o enquadramento teórico do DART está correto, com diálogo e transparência corretamente identificados como ausentes; o score de risco 4 é logicamente justificado pelo teor 'game-breaking' do título e pela ambivalência do autor, ponderado com seu trust level 3; e os metadados (ID, jogo, timestamp, likes, trust level, mapeamento de QIs) são consistentes com o contexto da análise.

---

### Post Auditado #14: `3000013_19863281` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais das dimensões DART estão presentes de forma exata no post original. O enquadramento conceitual de Diálogo, Acesso, Risco e Transparência segue corretamente as definições do framework. O score de risco percebido (5) está bem fundamentado na linguagem intensa e nas referências a danos financeiros e reputacionais. Os metadados (jogo, ID, mapeamento das QIs) são consistentes com o post analisado. Análise de alta qualidade, sem erros identificados.

---

### Post Auditado #15: `512885_2886318` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** As evidências literais citadas (como 'no interaction', 'no counterplay', 'no risk', 'Salt is supposed to be the byproduct of conflict, not the only reason the mechanic exists') existem literalmente no post. As interpretações estão conceitualmente alinhadas com as dimensões DART (Diálogo, Acesso, Risco e Transparência) conforme as definições clássicas. O score de risco 4 é bem fundamentado, pois o texto evidencia a perceção de uma mecânica desequilibrada e prejudicial. Os metadados (jogo, ID, QIs) são coerentes com o conteúdo e a análise.

---

### Post Auditado #16: `514029_2895732` — Score: **75/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** As evidências literais para as dimensões Acesso e Risco referem-se a frases que não constam no corpo do post original (apenas no título). As interpretações conceituais e a fundamentação do risco estão corretas, assim como a coerência dos metadados.

---

### Post Auditado #17: `3000008_25929662` — Score: **80/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **NÃO** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal citada para 'acesso' e 'risco' encontra‑se de facto no post original. O enquadramento teórico das dimensões DART está correto. Contudo, a fundamentação do score de risco percebido recorre a elementos externos ao texto (número de likes, trust level, edições) que não derivam diretamente da expressão de risco no post, comprometendo a lógica da justificação. O score em si (3) ainda é defensável face ao conteúdo, mas a argumentação não está puramente ancorada no texto, pelo que a fundamentação não é totalmente válida. Os metadados estão coerentes.

---

### Post Auditado #18: `511200_2873610` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A frase citada como evidência literal nas dimensões 'risco' e 'transparência' corresponde exatamente ao corpo do post original. A aplicação dos conceitos DART está alinhada com as definições clássicas: risco como percepção de perda de controlo e ameaça à integridade, transparência como questionamento da clareza dos critérios de moderação. O score de risco 4 é bem fundamentado pela credibilidade do utilizador (trust level 3) e pela gravidade da acusação de botting, mesmo com 0 likes. Os metadados (ID arbitrário, jogo, mapeamento para QI3, QI4, QI5) são coerentes com a análise, não havendo contradições. Todos os critérios estão satisfeitos.

---

### Post Auditado #19: `1t81ix0_3` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal para a dimensão Acesso está presente no post original, as demais dimensões sem evidência estão corretas. As definições conceituais do framework DART estão bem aplicadas: Diálogo ausente, Acesso vinculado à partilha de técnica para alternar clientes, Risco e Transparência não identificados. O score de risco 3 está bem fundamentado considerando a ambiguidade do título e a falta de menção explícita a riscos, com apoio nos metadados. Metadados consistentes com o jogo e mapeamento de QIs plausível. Não foram encontrados erros.

---

### Post Auditado #20: `3000006_27246271` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal do diálogo corresponde exatamente ao corpo do post. O enquadramento de diálogo como tentativa de manter coerência temática é consistente com o framework DART, mesmo num contexto de baixa interatividade. O score de risco 1 é adequado, pois o post não aborda riscos de forma explícita e o autor tem baixo capital social, sendo a referência a GDKP apenas um indício latente. Os metadados (jogo, ID, questões de investigação) estão coerentes com o conteúdo e o contexto do fórum.

---

### Post Auditado #21: `3000008_25930019` — Score: **80/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal para a dimensão 'acesso' é apresentada como 'People cant even afford raid consumes. the people buying gold can afford things'. Esta frase exata não consta de forma literal no post original, que tem: 'People cant even afford raid consumes because the market went right to whitemane era prices.' seguido de 'Incorrect, the people buying gold can afford things'. A concatenação e remoção de parte da frase original quebram a literalidade. Todas as outras dimensões apresentam evidências literais válidas e o enquadramento teórico, a fundamentação do risco e os metadados estão corretos e consistentes.

---

### Post Auditado #22: `512885_2886699` — Score: **80/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidencia_literal fornecida 'Shuttle Smart-bombing Is Anti-Gameplay, Not PvP ... That is way too much effort for today’s player.' não existe literalmente no corpo do post original, pois o corpo contém apenas a frase final e a citação de outro utilizador, mas não o título. A concatenação com '...' e a inclusão do título tornam o excerto não correspondente a qualquer substring do corpo, violando o requisito de evidência literal. As análises concetuais, a fundamentação do score de risco e a coerência dos metadados estão corretas.

---

### Post Auditado #23: `514029_2896810` — Score: **75/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal para a dimensão 'risco' ('Game-breaking lack of enforcement against input broadcasting / multi-input automation') provém do título do post original, mas não está presente no corpo do texto, violando o requisito de extração literal do corpo. As demais evidências ('player base that still remains seems to have shifted to this type of gameplay' e 'was unforeseeable at the time? Don’t know, just asking.') são literais do corpo. As interpretações conceituais estão alinhadas com o framework DART, a fundamentação do score de risco é coerente e os metadados estão consistentes com o post original.

---

### Post Auditado #24: `3000004_29505452` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal 'They’re vast criminal organisations' está presente no post original. As dimensões DART estão corretamente enquadradas: Diálogo, Acesso e Transparência ausentes, Risco presente com interpretação teórica adequada. O score de risco 4 é fundamentado de forma lógica, considerando a gravidade da ameaça ('organizações criminosas'), a ironia que sugere ineficácia das soluções e a credibilidade do usuário (trust level 3), mesmo com baixo engajamento (0 likes). Os metadados (jogo World of Warcraft, ID, QIs mapeadas como QI3 e QI5) são consistentes com o conteúdo. Nenhum erro detetado.

---

### Post Auditado #25: `509843_2862526` — Score: **85/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **NÃO** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal está corretamente vazia porque não há frases que suportem as dimensões. A fundamentação do risco percebido está lógica. Metadados coerentes. No entanto, há uma inconsistência conceptual: a 'dimensão dominante' é definida como 'dialogo', mas essa dimensão foi avaliada como não presente, o que contradiz a teoria DART.

---

### Post Auditado #26: `3000000_22980974` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências listadas são literais no post original. O enquadramento das dimensões DART está correto: Diálogo e Transparência ausentes, Risco presente e bem identificado. O score de risco 3 é justificado com base no conteúdo do post e no contexto comunitário. Os metadados (jogo, ID, QIs) são consistentes e coerentes com a análise.

---

### Post Auditado #27: `511200_2873992` — Score: **20/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **NÃO** | Risco Válido: **NÃO** | Metadados Coerentes: **NÃO**
* **Justificação do Auditor Académico:** Erro crítico: as evidências literais para Risco e Transparência foram extraídas do título do post ('Why is CCP punishing real players while looking the other way on botting?'), mas o corpo do post não contém essas frases. O corpo trata exclusivamente de um debate acalorado sobre argumentação, sem qualquer menção a bots, punições ou transparência da CCP. Portanto, 'evidencia_literal_existe' é falso para essas dimensões. A consistência conceitual falha porque Risco e Transparência são mapeados incorretamente a partir do título, não do conteúdo. A fundamentação do score de risco (4) baseia-se nessa evidência inexistente no corpo, invalidando-a. A presença errática dessas dimensões torna o mapeamento das QIs (QI3, QI4) inconsistente com o conteúdo real. Apenas Diálogo está corretamente identificado. A auditoria geral é negativa.

---

### Post Auditado #28: `510142_2865044` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais listadas existem exatamente no post original. As interpretações teóricas de Diálogo, Acesso, Risco e Transparência estão alinhadas com as definições clássicas do framework DART. O score de risco percebido (2) é bem fundamentado pelo texto do jogador (ausência de percepção de risco de sanção) e pelos metadados auxiliares. A coerência de metadados (jogo, ID, e mapeamento das QIs) está integralmente correta. Nenhum erro ou inconsistência foi detetado.

---

### Post Auditado #29: `509972_2863247` — Score: **75/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A auditoria revelou que a evidência literal para a dimensão ‘risco’ não está presente de forma exacta no post original. O texto do post contém ‘their chars teleported to Solitude after given a fair warning’, enquanto a análise cita ‘chars teleported to Solitude after given a fair warning’ (omissão do pronome ‘their’). Este pequeno desvio invalida a correspondência literal exigida. As restantes dimensões apresentam evidências literais válidas. Conceptual, a análise está correcta e alinhada com o framework DART. A fundamentação do score de risco (3) é coerente com o conteúdo. Os metadados (jogo, ID, QIs) são consistentes. Por isso, atribui-se uma pontuação de 75, penalizando apenas a não literalidade da evidência de risco.

---

### Post Auditado #30: `3000008_25925049` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais listadas ('Acesso', 'Risco', 'Transparência') existem exatamente no post original. As interpretações teóricas estão corretas e alinhadas com as definições do framework DART: Diálogo como ausência de interação bidirecional, Acesso como restrição a consumíveis, Risco como perceção de disfunção económica e Transparência como desconfiança na motivação da empresa. O score de risco 4 é bem fundamentado, considerando o impacto direto na acessibilidade e confiança, além de considerar o perfil do utilizador. Os metadados são coerentes: o jogo, ID do post, timestamp, likes, trust level e mapeamento das QIs (2,3,4,5) refletem corretamente as dimensões identificadas. A análise é precisa e completa.

---

### Post Auditado #31: `1675072_21541815` — Score: **75/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **NÃO**
* **Justificação do Auditor Académico:** Todas as frases de evidencia_literal existem de forma literal no post original. As interpretações DART estão alinhadas com os conceitos clássicos de diálogo, acesso, risco e transparência. O score de risco 4 é bem fundamentado com base no relato detalhado do jogador e no impacto sobre a integridade do jogo. No entanto, a análise omite a QI1 no mapeamento final (questoes_investigacao apenas inclui QI2, QI3, QI4, QI5), apesar de ter identificado a dimensão de diálogo como presente. Isso constitui uma inconsistência nos metadados, pois a QI relacionada ao diálogo não foi mapeada.

---

### Post Auditado #32: `509843_2862434` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** All literal evidence claims are present in the post. Conceptual framing accurately uses DART dimensions (Dialogue as request for information, Access as ability to use hauling route, Risk as potential abuse, Transparency as information need). Risk score 3 logically follows from the speculative tone and lack of community validation. Metadata (post_id, jogo, QIs) are consistent and correctly mapped. No errors found.

---

### Post Auditado #33: `11pmlty_5` — Score: **85/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** As evidências literais para 'acesso' (falta 'at,') e 'transparência' (falta '...') não são transcrições exatas do post original, violando o critério de literalidade. As interpretações conceituais, a fundamentação do score de risco (5) e os metadados estão corretos.

---

### Post Auditado #34: `511200_2873853` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais citadas estão presentes de forma literal no post original. As interpretações das dimensões Diálogo, Acesso, Risco e Transparência estão alinhadas com as definições clássicas do framework DART. O score de risco percebido (4) está logicamente fundamentado no conteúdo do post, refletindo a percepção de ameaça aos jogadores legítimos. Os metadados (jogo, ID, QIs) são consistentes com o post original. Nenhum erro detectado.

---

### Post Auditado #35: `3000008_25925050` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as frases de evidência literal estão presentes no corpo do post original ('botting and gold selling' e a frase completa para risco). As interpretações enquadram-se corretamente nos conceitos do DART: diálogo ausente, acesso relacionado a ferramentas de automação, risco como perceção de ameaça e transparência não mencionada. O score de risco 5 está bem fundamentado no tom categórico do post e nos metadados. Os metadados (jogo, ID, QIs mapeadas) são coerentes e consistentes com o conteúdo.

---

### Post Auditado #36: `509129_2863231` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal fornecida para a dimensão Risco ('We are most of the time complaining about the bots, and the dude you are aggroing was explaining that number is 'inflated'') está presente de forma exata no corpo do post original. As dimensões DART estão corretamente interpretadas segundo as definições clássicas: Diálogo, Acesso e Transparência são adequadamente classificados como ausentes, visto que o post não contém interação com agentes de IA/desenvolvedores, referências a APIs ou mecanismos de acesso, ou discussões sobre visibilidade de regras/algoritmos. A presença de Risco é bem identificada, alinhando-se ao conceito de incerteza e ameaça à integridade do ecossistema. O score de risco percebido (3) é logicamente fundamentado: o post menciona bots e números inflacionados, o que denota risco moderado à economia; o tom é apaziguador, o trust_level 3 indica experiência, e a ausência de likes sugere baixa validação social imediata, justificando uma classificação intermédia. Quanto aos metadados, o jogo 'EVE Online' está correto, o mapeamento para a QI3 (risco) é consistente com o conteúdo, e o post_id '509129_2863231' respeita a anonimização indicada. Portanto, a análise é integralmente válida, sem erros ou inconsistências.

---

### Post Auditado #37: `2035582_25942482` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais existem de forma exata no corpo do post. As interpretações de Diálogo, Acesso, Risco e Transparência estão corretas segundo as definições do framework DART. O score de risco percebido (3) está bem justificado, refletindo a perceção de risco moderado descrita no texto (balanço entre os danos atuais e os riscos comerciais da proposta). Os metadados (jogo, ID atribuído e mapeamento das QIs) são coerentes com o conteúdo e o contexto do fórum.

---

### Post Auditado #38: `511102_2872995` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A análise identifica corretamente apenas a dimensão Risco como presente, reproduzindo com exatidão as frases literais do post: 'massmultiboxing is part of that problem. Omnipresent Massmultiboxing is just one nail in that coffin.' As demais dimensões (Diálogo, Acesso, Transparência) estão ausentes, conforme o texto. A interpretação conceitual do Risco no contexto DART está correta, vinculando o mass multiboxing à degradação do ecossistema. O score de risco percebido 3 é coerente com o tom do post e a justificativa apresentada. Os metadados (jogo EVE Online, ID, QI3 e QI5) estão consistentes com o conteúdo.

---

### Post Auditado #39: `514029_2896815` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais estão presentes no título do post original. As interpretações teóricas estão alinhadas com as definições DART. O score de risco 5 é justificado pelo termo 'game-breaking' e pela quantificação dos ganhos. Os metadados (jogo, QIs, tipologia) estão coerentes com o conteúdo.

---

### Post Auditado #40: `3000003_28811596` — Score: **40/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **NÃO** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal corresponde exatamente ao corpo do post. O score de risco percebido (1) está bem justificado pela ausência de menção a riscos. Os metadados (jogo, ID, mapeamento de QIs) são coerentes. Contudo, a classificação do Diálogo como 'presente' é conceitualmente inconsistente com as definições do framework DART: o post é uma sugestão isolada, sem evidência de interatividade, escuta ou comunicação bidirecional exigida para caracterizar diálogo. A interpretação de uma proposta unilateral como 'diálogo iniciado pelo jogador' distorce o conceito, comprometendo a validade da análise. Por esse erro principal, a pontuação da auditoria é reduzida.

---

### Post Auditado #41: `3000000_22980837` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A frase 'if your selling stuff it hurts when gold is deflating' aparece de forma literal no post original. As dimensões Diálogo, Acesso e Transparência estão corretamente ausentes, dado que o texto não contém elementos desses tipos. A interpretação do Risco enquadra-se na definição teórica de risco económico decorrente da cocriação parasitária (bots) e a fundamentação do score 3 é lógica, considerando o impacto moderado na economia do jogo e os metadados (0 likes, Trust Level 2). A coerência dos metadados está confirmada: jogo, ID, timestamp, likes, trust_level e mapeamento das QIs (QI3 e QI5) são precisos.

---

### Post Auditado #42: `504046_2821673` — Score: **80/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **NÃO** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** As evidências literais listadas estão presentes no texto original. A conceitualização do Diálogo é inconsistente: uma única pergunta sem resposta visível não caracteriza dialogo autêntico segundo o modelo DART (o próprio analista admite falta de escuta ativa e negociação profunda). A fundamentação do risco está lógica e bem justificada. Metadados são coerentes.

---

### Post Auditado #43: `509129_2856914` — Score: **0/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **NÃO** | Risco Válido: **NÃO** | Metadados Coerentes: **NÃO**
* **Justificação do Auditor Académico:** Falha ao executar auditoria: Unterminated string starting at: line 7 column 29 (char 196)

---

### Post Auditado #44: `511200_2873732` — Score: **50/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** As evidências literais para as dimensões 'risco' ('Why is CCP punishing real players while looking the other way on botting?') e 'transparência' ('looking the other way on botting') foram extraídas do título do post, não do seu corpo, conforme exigido pelo critério. O corpo não contém essas frases. As evidências para 'diálogo' e 'acesso' estão corretas. As interpretações conceituais, a fundamentação do score de risco e os metadados do jogo e QIs são consistentes.

---

### Post Auditado #45: `2059924_26285238` — Score: **85/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **NÃO** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** As evidências literais listadas para Diálogo, Acesso e Risco estão presentes no post. Para Transparência, a ausência está corretamente indicada. A fundamentação do score de risco é lógica e consistente. Os metadados (jogo, ID, QIs) são coerentes. No entanto, a consistência conceitual do Acesso é frágil: a mera observação de bots não constitui 'acesso' no sentido clássico do DART, que se refere ao acesso a ferramentas, informação ou processos para co-criação. A interpretação de Diálogo é aceitável, mas o enquadramento de Acesso diverge. Por isso, a análise não é totalmente consistente conceitualmente, justificando a pontuação atribuída.

---

### Post Auditado #46: `1rvfe34_3` — Score: **75/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** As evidências literais listadas para as dimensões de Risco e Transparência ('Got permabanned for RMT out of nowhere, just paid for 2 years of Omega' e 'Got permabanned for RMT out of nowhere') constam apenas no título do post, e não no corpo ('Corpo: My wallet has like 20 million ISK...'). A exigência é que as frases estejam literalmente no corpo do post original, o que não se verifica. A consistência conceitual do DART, a fundamentação do score de risco (5) e a coerência dos metadados estão corretas. Por este motivo, a análise perde 25 pontos.

---

### Post Auditado #47: `511200_2873986` — Score: **80/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal para a dimensão 'acesso' é uma concatenação de duas frases não contíguas no post original ('I use tools to check my grammar and make sure I’m being clear.' e 'BTW I use translator + grammarly.'), não correspondendo a uma citação literal exata. As demais dimensões apresentam evidências presentes. A análise conceitual e os metadados estão corretos.

---

### Post Auditado #48: `3000006_27244798` — Score: **65/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **NÃO** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal existe para as dimensões 'acesso' e 'risco', e os metadados estão coerentes. A fundamentação do score de risco é válida e bem justificada. No entanto, a dimensão 'acesso' foi aplicada de forma inconsistente com o conceito original do framework DART, que diz respeito ao acesso a informação, ferramentas e interfaces para cocriação, e não à disponibilidade de recursos do jogo. O post não aborda acesso a ferramentas de cocriação, logo a presença marcada como 'true' para esta dimensão representa um erro conceitual significativo.

---

### Post Auditado #49: `1831388_23398084` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** As evidências literais de cada dimensão estão exatamente no post original. O enquadramento conceitual de Acesso e Risco está consistente com as definições do modelo DART adaptadas ao contexto de jogos. A fundamentação do score de risco 5 é lógica, baseando-se no colapso da rentabilidade e integrando métricas do post. Os metadados (jogo, QIs) são coerentes com a análise.

---

### Post Auditado #50: `3000000_22981406` — Score: **40/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **NÃO** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal para a dimensão 'Risco' não é uma citação contígua do post; combina duas frases separadas com reticências, não constituindo um excerto verbatim único. Conceitualmente, a análise interpreta 'Diálogo' como comunicação entre jogadores, quando o framework DART pressupõe interação humano-IA ou humano-desenvolvedor; o 'Risco' é enquadrado como risco económico do jogo, e não como risco percebido no uso de funcionalidades com IA. Estes desvios violam as definições clássicas. A pontuação de risco (2) está internamente justificada com base no texto, e os metadados são coerentes. Por estas razões, a análise é parcialmente válida mas falha em critérios fundamentais.

---

### Post Auditado #51: `3000001_22609261` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais correspondem exatamente a trechos do post original (incluindo o título). O enquadramento teórico das dimensões DART está correto: Diálogo avaliado como monólogo (ausência bidirecional), Acesso identificado pela menção a bots e RMT, Risco captado pelo temor de infestação, Transparência inferida da crítica à falta de ações visíveis dos desenvolvedores. O score de risco 5 é plenamente justificado pelo tom alarmista e pela generalização da inevitabilidade dos bots. Os metadados (jogo, ID, questões de investigação) estão coerentes. Análise de alta qualidade, sem erros.

---

### Post Auditado #52: `3000001_22609991` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais (diálogo, acesso, risco) estão presentes textualmente no post original. As interpretações conceituais alinham-se corretamente com as definições DART: diálogo entre jogadores, acesso a bots e automação, risco elevado de infestação. A transparência foi corretamente assinalada como ausente. O score de risco 5 está bem fundamentado no tom do autor e na falta de confiança na Blizzard. Os metadados (jogo, ID, QIs mapeadas) são consistentes com o contexto do post.

---

### Post Auditado #53: `3000008_25925089` — Score: **75/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **NÃO** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais citadas existem exatamente no post original. A fundamentação do score de risco 3 está lógica e bem justificada, e os metadados (jogo, ID, questões de investigação) são coerentes. No entanto, a dimensão 'Acesso' é conceptualmente inconsistente: o uso de GDKPs como ferramenta de equalização económica não se alinha com a definição clássica de Acesso no modelo DART, que se refere ao fornecimento de acesso a informações, dados ou ferramentas pela empresa para cocriação de valor. Aqui, trata-se de um sistema criado por jogadores, não oferecido pela Blizzard, o que invalida o enquadramento teórico dessa dimensão.

---

### Post Auditado #54: `3000004_29505453` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A análise está em total conformidade. As evidências literais existem exatamente no post original (corpo e título). O enquadramento conceitual de Diálogo e Risco está correto, e as ausências de Acesso e Transparência são adequadas. A pontuação de risco 4 é bem justificada pela complexidade mencionada. Os metadados (jogo, QIs mapeadas) são consistentes.

---

### Post Auditado #55: `511200_2872836` — Score: **30/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** As frases de evidência literal listadas em 'Diálogo', 'Acesso', 'Risco' e 'Transparência' não se encontram no corpo do post original. Todas as alegações de evidência baseiam‑se no título ou em combinações que incluem o título, enquanto a auditoria exige presença literal no corpo da mensagem. Isto compromete a validade da análise. Apesar de a consistência teórica das definições DART estar correta e a fundamentação do risco percebido fazer sentido considerando o texto completo (título + corpo), a ausência total de evidência literal de suporte é uma falha crítica que reduz substancialmente a pontuação.

---

### Post Auditado #56: `513682_2897017` — Score: **80/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal para as dimensões 'acesso' e 'risco' é apresentada como concatenações de fragmentos ('input broadcasting programs ... alt-tab / eve-o / windows cascade clicking' e 'Add a hard-coded client switching delay ... to motivate players who are not cheating to cheat? ... This just smell as another stupid ganking nerf') que não existem como frases únicas e literais no post, embora os elementos individuais estejam presentes. As definições conceituais das dimensões DART estão corretas. A fundamentação do score de risco está alinhada com o conteúdo e é lógica. Os metadados estão coerentes. A qualidade geral da análise é boa, mas a não literalidade exata no 'evidencia_literal' reduz ligeiramente a pontuação.

---

### Post Auditado #57: `509972_2863341` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais citadas existem exatamente no post original. As interpretações teóricas de Diálogo (ausente, pois é comunicação unidirecional), Acesso (restrição assimétrica), Risco (ameaça à integridade do conteúdo) e Transparência (opacidade percebida) estão corretamente alinhadas às definições do framework DART. O score de risco 3 (moderado) é bem fundamentado com base no conteúdo (preocupação com destruição, mas regras já existem) e nos metadados (trust level 2, 0 likes). O mapeamento para as QIs 2, 3, 4 e 5 é coerente, e o jogo EVE Online está consistente. Nenhum erro foi identificado.

---

### Post Auditado #58: `511102_2896964` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as citações são literais e presentes no post original. As interpretações conceituais das dimensões Diálogo, Acesso, Risco e Transparência estão alinhadas com o framework DART. O score de risco 4 é consistente com o conteúdo e bem fundamentado. Os metadados são coerentes com o post e as QIs mapeadas adequadamente.

---

### Post Auditado #59: `511004_2872594` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** As evidências literais citadas para Acesso e Risco existem exatamente no post original. A análise conceitual está alinhada com as definições de Diálogo, Acesso, Risco e Transparência. O score de risco 4 é justificado de forma clara e razoável face ao conteúdo do post. Os metadados (jogo, ID atribuído, mapeamento de QIs) são coerentes e sem inconsistências. Nenhum erro detetado.

---

### Post Auditado #60: `513682_2892720` — Score: **60/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **NÃO** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** O critério de evidência literal não é cumprido: a frase listada para a dimensão Acesso ('Input broadcasters or similar programs!') encontra-se no título e não no corpo do post original, violando a exigência de que a evidência deve existir literalmente no corpo. A consistência concetual é fraca: a dimensão Diálogo é tida como presente, mas o post não evidencia interação dialógica genuína — é sobretudo uma afirmação pessoal sobre perícia, o que não se enquadra na definição clássica de diálogo interativo. O score de risco (3) e a sua fundamentação são válidos e estão em linha com o conteúdo. Os metadados (jogo, ID e mapeamento das QI) estão coerentes.

---

### Post Auditado #61: `3000012_25620442` — Score: **75/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal da dimensão Acesso ('players that take short cuts. GDKPers that dont have the time to farm gold') não é uma substring exata do post original, que contém 'players that take short cuts. GDKPers that “dont have the time to farm gold”' (com aspas). A evidência literal da dimensão Risco inclui 'bots still wrecked the AH', que não aparece textualmente; o post diz 'they still wrecked the AH' referindo-se a bots indiretamente. Apesar disso, as interpretações conceituais DART estão corretas, a fundamentação do score de risco (5) é lógica e os metadados são coerentes. Por essa imprecisão nas evidências literais, a análise perde pontos, mas mantém qualidade geral.

---

### Post Auditado #62: `1t81ix0_6` — Score: **70/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **NÃO** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal citada ('pretty easy to see how it works without breaking any rules') existe exatamente no post. A fundamentação do risco percebido (4/5) é lógica e coerente com o contexto de EVE Online. Os metadados estão coerentes. Contudo, a dimensão 'Diálogo' foi mal enquadrada conceitualmente: segundo as definições clássicas de DART, diálogo exige interatividade e bilateralidade, enquanto o post é um compartilhamento unidirecional de informação entre jogadores, não configurando um ato de diálogo com a empresa ou mesmo um diálogo estruturado entre pares. A interpretação teórica forçada compromete a consistência conceitual.

---

### Post Auditado #63: `xaonz7_10` — Score: **85/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal na dimensão Risco apresenta uma citação composta por duas frases não contíguas no texto original ('Botting is a pretty serious issue, but treating players as bots is also a pretty serious issue. if it does then the bots are going to win based on the law of averages.'), o que viola o critério de existência de uma única sequência literal contínua. As demais evidências são literais, e as interpretações conceituais, score de risco e metadados estão corretos. Dedução de 15 pontos por essa não conformidade.

---

### Post Auditado #64: `512885_2886347` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais apresentadas ('Let’s just go with “no”' e 'don’t load shuttles up with expensive sh*t') constam exatamente no corpo do post original. A análise conceitual do Diálogo e do Risco segue as definições clássicas do DART, identificando corretamente a presença de diálogo e risco com interpretações adequadas. O score de risco percebido (3) está bem fundamentado, apoiando-se no conteúdo do post, no perfil de confiança do autor e na ausência de engajamento, com uma lógica coerente de mitigação. Os metadados são consistentes: o jogo ('EVE Online'), o ID gerado e o mapeamento das QIs (QI1, QI3, QI5) refletem com precisão as dimensões encontradas, sem discrepâncias.

---

### Post Auditado #65: `509129_2862258` — Score: **90/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal para Transparência ('Team Security [ID_ANONYMIZED] Bans ... 4k in Feb, 6k in March. 8k in April maybe??') mistura título e corpo com reticências não presentes no post original, não constituindo uma citação exata do corpo. As restantes evidências, a interpretação conceitual DART, a fundamentação do score de risco e a coerência dos metadados estão corretas.

---

### Post Auditado #66: `509129_2863220` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais apresentadas para Diálogo, Risco e Transparência constam literalmente no post original. As dimensões DART foram aplicadas de forma conceitualmente correta: há diálogo crítico, risco percebido elevado e denúncia de falta de transparência. O score de risco 4 está bem fundamentado pela alegação de que 95% dos bots não são afetados. Os metadados (jogo, ID, QIs) estão coerentes entre o post e a análise. Nenhum erro encontrado.

---

### Post Auditado #67: `509129_2863223` — Score: **60/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **NÃO** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal está correta: as frases indicadas existem no post. A coerência de metadados é válida. A fundamentação do score de risco é lógica. No entanto, a consistência conceitual falha nos seguintes pontos: (1) Diálogo: no quadro DART clássico, diálogo refere-se à interação direta e interessada entre empresa e consumidor, não a um debate indireto entre jogadores sobre a empresa; a análise interpreta erroneamente uma discussão entre pares como diálogo DART. (2) Risco: o conceito de risco em DART diz respeito ao risco partilhado na cocriação de valor, não ao risco genérico de integridade do jogo por bots. A análise equipara “risco de muitos bots” a risco DART, o que é um desvio conceitual. (3) Transparência: a análise afirma que a transparência está presente, mas na realidade o post evidencia uma assimetria de informação (a CCP sabe mais), o que configura falta de transparência. A atribuição de 'presente: true' e a interpretação subsequente não respeitam a definição clássica de transparência como informação simétrica e disponível. Pontos fortes: evidência literal correta, metadados coerentes e justificação do score de risco válida.

---

### Post Auditado #68: `509843_2862521` — Score: **0/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **NÃO** | Risco Válido: **NÃO** | Metadados Coerentes: **NÃO**
* **Justificação do Auditor Académico:** Falha ao executar auditoria: Expecting value: line 1 column 1 (char 0)

---

### Post Auditado #69: `514029_2895580` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as frases de evidência listadas para cada dimensão DART estão presentes literalmente no post original. As interpretações teóricas estão alinhadas com os conceitos clássicos do framework: Diálogo como feedback indireto, Acesso como uso de ferramentas disponíveis, Risco como potencial violação de regras e Transparência como abertura do jogador. A fundamentação do score de risco (4) é lógica, baseada na exposição pública de uma prática de zona cinzenta e no contexto do tópico sobre falta de enforcement. Os metadados (jogo, ID, questões de investigação) são coerentes e consistentes. Nenhuma incongruência encontrada.

---

### Post Auditado #70: `3000010_25329928` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais (para risco e transparência) estão presentes de forma exata no post original. As dimensões DART estão corretamente identificadas segundo os conceitos clássicos: ausência de diálogo e acesso, presença de risco e transparência bem fundamentados. O score de risco 5 é justificado pela ameaça à integridade da conta e à confiança no sistema, consistente com o teor do post. Os metadados (jogo, ID, mapeamento de QIs) são coerentes, com QI3 para risco, QI4 para transparência e QI5 para cocriação, refletindo as dimensões presentes.

---

### Post Auditado #71: `510142_2864742` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais citadas existem de forma literal no post original (corpo e título). A aplicação das dimensões DART está correta: Diálogo como tentativa de comunicação, Risco associado à mineração passiva, Acesso e Transparência ausentes, conforme as definições canónicas. O score de risco 4 está bem fundamentado na proposta drástica do jogador e na contextualização dos metadados. Metadados como ID, jogo e QIs são consistentes entre si e com a análise.

---

### Post Auditado #72: `504512_2824277` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais citadas na análise (frases sobre diálogo e risco) foram encontradas textualmente no post original. O enquadramento conceitual das dimensões Diálogo e Risco está alinhado com as definições de Prahalad & Ramaswamy, e a dimensão Acesso e Transparência estão corretamente ausentes. O score de risco 4 é justificado de forma lógica com base na descrição do jogador de operações 'risk free' e na escalada da vulnerabilidade por espionagem, e a fundamentação detalha essa lógica. Os metadados (jogo, ID, QIs mapeadas) estão coerentes: diálogo com QI1, risco com QI3, e a cocriação da experiência com QI5 são pertinentes.

---

### Post Auditado #73: `511004_2872749` — Score: **95/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** As evidências literais para Diálogo e Risco estão presentes na íntegra no post original. A evidência de Acesso, embora ligeiramente comprimida com elipse, captura corretamente as frases-chave. A interpretação teórica segue rigorosamente o framework DART. A fundamentação do score de risco 4 é lógica e bem justificada. Os metadados (jogo, ID, QIs) são coerentes. Pequena imprecisão no formato da citação de acesso não compromete a análise geral.

---

### Post Auditado #74: `504046_2822018` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A análise classificou corretamente todas as dimensões DART como ausentes, uma vez que o post não contém interação com IA ou desenvolvedores, apenas negociação entre humanos. As evidências literais não foram inventadas (strings vazias). As definições conceituais foram respeitadas (Diálogo exige IA, etc.). O score de risco 1 é bem justificado com base na ausência de menção a risco, baixo nível de confiança e visibilidade social reduzida, mas alta normalidade da transação em EVE Online. Os metadados (ID, jogo, likes, trust level, edições) são coerentes com o contexto e a análise não inclui mapeamento forçado a questões de investigação, o que é adequado.

---

### Post Auditado #75: `511004_2872732` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais citadas aparecem literalmente no post original. O enquadramento das dimensões DART está correto segundo as definições de Prahalad & Ramaswamy, com interpretações adequadas. A fundamentação do score de risco 5 é lógica e baseada no texto, justificando-se pela gravidade e volume dos riscos descritos. Os metadados (jogo, ID, QIs) são coerentes. A análise demonstra alta qualidade e aderência aos critérios.

---

### Post Auditado #76: `1hs6hm3_10` — Score: **90/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A análise está correta em todas as dimensões, com exceção da evidência literal para a dimensão Risco. A frase citada como 'evidencia_literal' não corresponde exatamente ao texto original: omite um 'so' ('so so far' no original vs. 'so far' na análise). Todos os outros aspetos (consistência conceitual, fundamentação do risco e coerência de metadados) estão válidos.

---

### Post Auditado #77: `511200_2872977` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais constam exatamente no post original. O enquadramento DART está conceitualmente correto: o diálogo é configurado como comunicação assimétrica entre jogador e desenvolvedora; o acesso reflete restrições a rendimentos legítimos; o risco descreve danos económicos percebidos; a transparência evidencia a desconfiança nas ações da CCP. A fundamentação do score de risco (4) assenta em argumentos lógicos e coerentes com o conteúdo apresentado, incluindo a consideração de trust level e engajamento social. Os metadados (jogo, ID, questões de investigação) estão todos consistentes com o post e o modelo de análise.

---

### Post Auditado #78: `514029_2895225` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todos os critérios foram atendidos: as evidências literais existem exatamente no post original; as interpretações das dimensões DART (diálogo, risco, transparência) estão alinhadas com as definições clássicas; a justificação do score de risco 4 é lógica e baseada no texto e metadados; os metadados (jogo, ID, mapeamento de QIs) são internamente consistentes e correspondem ao post.

---

### Post Auditado #79: `xaonz7_2` — Score: **40/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **NÃO** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal de 'risco' e 'transparência' não corresponde a frases exatas do post: a de 'risco' usa reticências para omitir 'I said this in other post but botting in EVE is like crypto mining.' e a de 'transparência' omite 'they are so deep in shit', quebrando a literalidade. A conceptualização de Acesso está equivocada, pois no framework DART o acesso refere-se a recursos disponibilizados pela empresa para cocriação, e não a mercados ilícitos como o RMT. Os scores de risco e metadados estão corretos e bem justificados.

---

### Post Auditado #80: `1uq9f5i_4` — Score: **65/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal para a dimensão Acesso ('Hackers are engineering botting in Darktide') não está no corpo do post, apenas no título. A evidência para Risco ('If Botting comes for Darktide... This is just the current beta😞😕') combina corpo e título, sendo que a parte 'This is just the current beta😞😕' também não consta do corpo. Apenas a evidência de Diálogo é literalmente do corpo. Isso viola o critério de existência literal no corpo do post original. As demais análises conceituais, de risco e metadados estão corretas.

---

### Post Auditado #81: `510142_2864984` — Score: **95/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A análise captura adequadamente a presença de Diálogo, Acesso e Risco, com interpretações coerentes com o framework DART. A ausência de Transparência está correta. As evidências literais listadas são paráfrases aproximadas dos trechos exatos do post, não reproduções literais contíguas, mas os fragmentos-chave existem no texto original. O score de risco 4 é bem justificado pelo conteúdo ('stagnant meta', 'lower quality content'). Metadados (jogo, ID, QIs) são consistentes com o contexto. Pequena imprecisão na literalidade reduz a pontuação de 100 para 95.

---

### Post Auditado #82: `510142_2865257` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todos os critérios foram aprovados. As evidências literais selecionadas para Acesso e Risco estão contidas no post original, com a evidência de Acesso apresentando uma pequena inversão de ordem que mantém todas as palavras exatas. O enquadramento teórico DART (Diálogo, Acesso, Risco, Transparência) foi aplicado corretamente. O score de risco 5 está devidamente fundamentado na linguagem extrema do autor ('pure cancer for the game') e no contexto do trust level elevado. Os metadados (jogo, mapeamento das questões de investigação, IDs) são consistentes.

---

### Post Auditado #83: `509843_2862470` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais fornecidas para Acesso, Risco e Transparência existem de forma exata e contígua no post original. A interpretação dos conceitos DART está alinhada com as definições clássicas: diálogo ausente, acesso limitado, risco de colapso económico e falta de transparência. A pontuação de risco (4) está bem fundamentada, considerando a gravidade da acusação e o perfil do utilizador. Os metadados (jogo, ID, mapeamento das QIs) são plenamente consistentes com o conteúdo.

---

### Post Auditado #84: `3000007_29299356` — Score: **90/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal para a dimensão 'diálogo' contém reticências e omite parte da frase, não sendo uma citação exata do post original. As demais evidências literais são válidas. O enquadramento teórico, a fundamentação do risco e a coerência dos metadados estão corretos.

---

### Post Auditado #85: `511200_2874001` — Score: **70/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal para a dimensão 'transparencia' ('Why is CCP punishing real players while looking the other way on botting?') não está contida no corpo do post original, que corresponde estritamente ao texto fornecido. A frase só aparece no título, violando o critério de existência literal no corpo. As demais dimensões, o score de risco e os metadados estão corretos. Por isso, a auditoria penaliza esse erro, mas considera a análise globalmente aceitável.

---

### Post Auditado #86: `511200_2873752` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as strings de evidência listadas aparecem literalmente no post original (título ou corpo). As interpretações conceituais de Diálogo, Risco e Transparência estão alinhadas com as definições do DART, e a ausência de Acesso é corretamente identificada. O score de risco percebido (5) está adequadamente fundamentado nos argumentos do post, que expressam alto risco para jogadores legítimos caso o EAC seja implementado. Os metadados (jogo 'EVE Online', ID e mapeamento das QIs) são internamente consistentes e compatíveis com o conteúdo analisado.

---

### Post Auditado #87: `3000001_22609513` — Score: **85/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal da dimensão Risco não corresponde exatamente ao texto original; a análise apresenta 'outcome is determined by whoever has the fewer bots' quando o post original diz 'the pvp outcome is determined by whoever has the fewer bots'. As demais evidências são literais. A consistência conceitual está correta, a fundamentação do score de risco é válida, e a coerência dos metadados (jogo, QIs) mantém-se, embora o ID não seja verificável.

---

### Post Auditado #88: `512885_2886502` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal citada existe exatamente no post original. A interpretação da dimensão Diálogo está conceitualmente correta, e as demais dimensões foram corretamente identificadas como ausentes. A fundamentação do score de risco percebido (2) é lógica e coerente com o conteúdo do post. Os metadados (jogo, ID, QIs) são consistentes.

---

### Post Auditado #89: `xaonz7_7` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A análise apresenta evidências literais extraídas corretamente para acesso e risco, não havendo diálogo ou transparência no post. A consistência conceitual com o framework DART está correta, com interpretações apropriadas. O score de risco percebido 5 é justificado pela gravidade da sugestão envolvendo fraude real. Os metadados (jogo, QIs, tipologia) são coerentes. Nenhum erro detectado.

---

### Post Auditado #90: `499582_2788175` — Score: **80/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal da dimensão 'risco' apresenta uma ligeira imprecisão: o post original menciona 'bots' e não 'botting' ("That way bots, AFK solo mining..."). Embora o significado seja equivalente, não é uma citação literal exata, o que viola o critério de existência literal. Todos os outros critérios são cumpridos: as dimensões DART estão enquadradas corretamente, o score de risco percebido 5 é bem fundamentado pela linguagem veemente do autor, e os metadados (jogo, ID, QIs) são coerentes. Por conseguinte, a auditoria atribui 80 pontos, penalizando apenas a falha na transcrição literal.

---

### Post Auditado #91: `514029_2895231` — Score: **85/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal da dimensão Diálogo contém texto adicional não presente literalmente no post original ("(cited developer statement) - player posts to forum seeking action"). As demais dimensões apresentam evidências literais corretas. A consistência conceitual, a fundamentação do score de risco e a coerência dos metadados estão adequadas.

---

### Post Auditado #92: `3000004_29505438` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A análise está correta e bem fundamentada. A evidência literal 'vast criminal organisations' existe exatamente no corpo do post. As dimensões DART foram aplicadas de forma consistente com os conceitos teóricos (apenas Risco presente, justificadamente). O score de risco 5 é coerente com a gravidade da expressão utilizada e o contexto do jogo, com justificação lógica. Os metadados (jogo, ID, QIs mapeadas) são precisos e coerentes com o conteúdo do post.

---

### Post Auditado #93: `488781_2730194` — Score: **62/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **NÃO** | Risco Válido: **SIM** | Metadados Coerentes: **NÃO**
* **Justificação do Auditor Académico:** A evidência literal é exata, reproduzindo o texto do post. A fundamentação do score de risco (4) está coerente com a queixa. No entanto, a análise força o conceito de diálogo (presente) quando o post é apenas uma reclamação unidirecional sem interação nem resposta, violando a definição de diálogo como cocriação bidirecional. Adicionalmente, a listagem das questões de investigação omite QI1 (relativa a diálogo) apesar de alegar a presença dessa dimensão, gerando incoerência entre as dimensões mapeadas e as QIs. Estes erros reduzem a consistência geral.

---

### Post Auditado #94: `11pmlty_10` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as frases de evidência literal existem exatamente no post original. As interpretações das dimensões DART (Diálogo falhado, Risco elevado, Transparência nula, Acesso ausente) estão alinhadas com as definições clássicas do framework. A fundamentação do score de risco percebido 5 é lógica e coerente com o texto e metadados. Os metadados (jogo, post_id, QIs mapeadas) estão consistentes. Nenhum erro detetado.

---

### Post Auditado #95: `3000002_27798197` — Score: **70/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal para a dimensão Risco não coincide exatamente com o texto do post: a frase 'game was about to die! then blizzard allowed bots again to save the game from dying.' não existe literalmente, pois o post original contém 'to run' entre 'allowed bots again' e 'to save...'. As demais evidências (Acesso e Transparência) são literais. A conceção teórica de Diálogo, Acesso, Risco e Transparência está correta segundo as definições clássicas. A fundamentação do score de risco (3) é coerente com o conteúdo e os metadados (jogo, ID, QIs) são consistentes. A análise é válida, mas a transcrição imprecisa compromete parcialmente a fidelidade dos dados.

---

### Post Auditado #96: `3000007_29299434` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais fornecidas existem no corpo do post original. As interpretações conceituais estão alinhadas com as definições do framework DART (diálogo bidirecional, acesso a ferramentas, risco percebido, transparência de processos). O score de risco 4 é bem fundamentado pela linguagem emocional e pelo impacto direto na jogabilidade solo, apesar do baixo engajamento social. Os metadados (jogo, ID, QIs) são coerentes com a análise e com o post. Nenhuma inconsistência detetada.

---

### Post Auditado #97: `504512_2824478` — Score: **70/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **NÃO** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais listadas para Diálogo, Acesso, Risco e Transparência foram encontradas exatamente no post original, cumprindo o primeiro critério. A fundamentação do score de risco (5) está bem justificada com base na linguagem catastrófica do autor e nos metadados de confiança. Os metadados (jogo, ID, QIs) são coerentes. No entanto, o enquadramento do Diálogo como 'presente' não é consistente com as definições clássicas do framework DART, que exigem interatividade bilateral e engajamento mútuo; o post é uma reclamação unidirecional sem indícios de resposta ou diálogo efetivo, pelo que a consistência conceitual é incorreta. A pontuação reflete a qualidade geral parcialmente comprometida pelo erro conceitual.

---

### Post Auditado #98: `3000009_28801061` — Score: **75/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal para a dimensão 'transparência' ('Does Microsoft use any of its A.I. technology for anything related to World of Warcraft?') não se encontra no corpo do post original, apenas no título. As restantes evidências, consistência conceitual, fundamentação do risco e coerência de metadados estão corretas. A análise é sólida, mas falha num critério de auditoria.

---

### Post Auditado #99: `3000008_25925197` — Score: **70/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **NÃO** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** As evidências literais citadas existem exatamente como transcritas do post original. A fundamentação do score de risco (5) é válida, apoiada em provas concretas e lógica contextual. Os metadados (jogo, ID, QIs) estão coerentes. No entanto, a dimensão 'acesso' foi interpretada de forma equivocada: no framework DART clássico (Prahalad & Ramaswamy), o Acesso refere-se à capacidade do consumidor de utilizar ferramentas e informações fornecidas pela empresa, não à posse interna de dados pela empresa. A análise descreve o acesso unilateral da Blizzard, o que não se alinha com a definição canónica. Esta inconsistência conceitual reduz a validade teórica da análise, justificando o score 70.

---

### Post Auditado #100: `1t81ix0_4` — Score: **0/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **NÃO** | Risco Válido: **NÃO** | Metadados Coerentes: **NÃO**
* **Justificação do Auditor Académico:** Falha ao executar auditoria: Expecting value: line 1 column 1 (char 0)

---

### Post Auditado #101: `3000013_19862910` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal citada em 'risco' consta exatamente no corpo do post. As dimensões do DART foram corretamente classificadas (Diálogo, Acesso e Transparência ausentes; Risco presente). O score de risco 4 é bem justificado pela citação de impacto regular em BGs, e os metadados (ID, jogo, QIs) são consistentes e mapeados adequadamente.

---

### Post Auditado #102: `1t81ix0_2` — Score: **0/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **NÃO** | Risco Válido: **NÃO** | Metadados Coerentes: **NÃO**
* **Justificação do Auditor Académico:** Falha ao executar auditoria: Expecting value: line 1 column 1 (char 0)

---

### Post Auditado #103: `514029_2896923` — Score: **60/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **NÃO** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal para a dimensão 'risco' ('Game-breaking lack of enforcement against input broadcasting / multi-input automation') pertence ao título do post, não ao corpo. O corpo fornecido contém apenas 'Eaglefeather: handed over the keys...' e 'Security through obscurity...', sem essa frase. Como a auditoria exige que a evidência exista literalmente no corpo do post, esta falha compromete a validade da fundamentação do score de risco (que se baseia nessa acusação de 'game-breaking'). As demais dimensões estão conceitualmente corretas e os metadados consistentes, mas a falha na evidência principal reduz a qualidade geral.

---

### Post Auditado #104: `3000004_29506491` — Score: **70/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **NÃO** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** As evidências literais para diálogo e risco existem no texto original. A fundamentação do score de risco está coerente. Porém, a dimensão 'diálogo' foi classificada como presente com base em uma interação sarcástica entre utilizadores, o que não se alinha com a definição teórica do DART, que enfatiza o diálogo ativo entre consumidor e empresa. Portanto, há inconsistência conceitual. Metadados e mapeamento de QIs estão corretos.

---

### Post Auditado #105: `2076631_26504845` — Score: **65/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal para a dimensão 'risco' contém imprecisões: a frase 'Botting is actively degrading the game experience and economy.' não está literalmente no post (o post refere 'it is actively degrading...'), e a frase 'Server instability persists.' não existe no post. As outras dimensões têm evidência literal correta. A consistência conceitual está adequada aos princípios DART. A fundamentação do risco percebido é válida e justifica o score 5. Os metadados são coerentes. Porém, devido à falha de literalidade, a análise perde rigor, resultando numa pontuação de 65.

---

### Post Auditado #106: `512885_2886553` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais citadas constam literalmente no post original. As dimensões DART estão corretamente interpretadas: diálogo como interação entre pares no fórum, risco associado à mecânica de smart‑bombing e sua mitigação, ausência de acesso e transparência. A pontuação de risco percebido (2) está bem fundamentada na postura do autor, que minimiza o perigo, com ressalvas contextuais apropriadas. Os metadados (jogo, QIs mapeadas) são coerentes com o conteúdo e o framework. Nenhuma inconformidade detetada.

---

### Post Auditado #107: `487448_2723683` — Score: **93/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A análise apresenta evidência literal correta para a dimensão 'risco', a frase 'the economy is also worse than ever' existe no post original. A interpretação teórica com referência a Slovic (1987) é consistente com a definição de risco no framework DART. O score de risco 3 está bem fundamentado, considerando a preocupação moderada e a relativização do jogador. Os metadados (jogo, QIs, post_id, likes, trust level) são coerentes com o post. Apenas uma pequena ressalva: a alocação da QI5 (cocriação de valor) é ligeiramente tangencial, mas não compromete a validade geral, uma vez que a observação económica pode indiretamente relacionar-se com a cocriação de valor no ecossistema de EVE Online. No geral, a análise é sólida e reflete corretamente o conteúdo e o framework.

---

### Post Auditado #108: `513682_2892459` — Score: **95/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** As três evidências literais de diálogo, acesso e transparência estão exatamente no post original. A evidência de risco está presente, mas com uma diferença de capitalização ('players' vs. 'Players'), o que impede uma correspondência literal perfeita. As interpretações DART são conceitualmente corretas. A fundamentação do score de risco (5) está bem justificada pelo texto do post. Metadados (jogo, ID, QIs) são coerentes. Dedução de 5 pontos pela imprecisão na transcrição exata da evidência de risco.

---

### Post Auditado #109: `18m0xzk_7` — Score: **85/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal indicada na dimensão Risco ('someone bought out all the rigs and then tripled the price. … very rarely works out well') não existe de forma exata no corpo do post original, pois combina uma frase do título e outra do corpo com uma elipse. Embora ambos os segmentos apareçam separadamente, a exigência de literalidade não é cumprida. As restantes verificações são positivas: a análise conceitual das dimensões DART é consistente, o score de risco está bem fundamentado e os metadados são coerentes. Dedução de 15 pontos por esta falha na evidência literal.

---

### Post Auditado #110: `1guy1bx_3` — Score: **90/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal para Transparência ('Botting ok. ... BAN. logic!') não é uma transcrição exata do post original, que contém o travessão e o texto integral 'Botting ok.- say one bad thing in barren chat. BAN. logic!'. A omissão com reticências compromete a exigência de literalidade. As demais dimensões e metadados estão corretos e bem fundamentados, pelo que a auditoria deduz 10 pontos.

---

### Post Auditado #111: `514029_2896854` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A auditoria confirma que todas as evidências literais citadas existem integralmente no post original (diálogo, acesso e risco). A aplicação do framework DART está correta conceitualmente, respeitando as definições de diálogo, acesso, risco e transparência. O score de risco percebido (2) é fundamentado de forma lógica, equilibrando o título alarmista com a postura moderada do autor e a ausência de validação da comunidade. Os metadados (jogo, ID do post e mapeamento das QIs) são coerentes com o conteúdo analisado. Não foram identificados erros.

---

### Post Auditado #112: `3000004_29505617` — Score: **80/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal para as dimensões 'dialogo' e 'risco' inclui a frase 'I bet Blizzard could get rid of 99% of botters and scammers by just', que pertence ao título e não está presente no corpo do post original. Apenas a evidência de 'transparencia' ('Hiring like 3 guys...') encontra-se literalmente no corpo. Como as frases listadas em evidencia_literal devem existir no corpo, este critério não é cumprido na totalidade. Os restantes critérios estão corretos: a consistência conceitual das dimensões DART é adequada, o score de risco está bem fundamentado e os metadados são coerentes. Penalização leve por incumprimento parcial da literalidade da evidência.

---

### Post Auditado #113: `499582_2788505` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais listadas na análise estão presentes de forma exata no texto do post original. As interpretações teóricas das dimensões Acesso e Risco estão alinhadas com as definições do framework DART. O score de risco percebido 3 é bem fundamentado, refletindo a postura moderada do utilizador ao reconhecer o botting como batota e sugerir a denúncia. Os metadados (jogo, ID do post, questões de investigação) são consistentes com o conteúdo e com a análise realizada.

---

### Post Auditado #114: `499582_2789504` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** As evidências literais para Diálogo, Acesso, Risco e Transparência foram todas encontradas de forma exata no post original. O enquadramento conceitual de cada dimensão do DART está correto: Diálogo captura a discussão sobre design; Acesso, embora interpretado como gestão de múltiplas contas, é uma leitura válida no contexto de recursos do jogador; Risco é apropriadamente rotulado como operacional e baixo; Transparência reflete a clareza da mecânica. O score de risco (2) é coerente com o texto que minimiza a perda de yield e propõe contorno via novas contas. Os metadados (jogo, ID, QIs) são consistentes e mapeiam adequadamente as dimensões e a tipologia assimétrica da cocriação.

---

### Post Auditado #115: `499582_2791002` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** O post original contém exatamente a frase 'Neglecting real updates just to spite multiboxers is dumb.' usada como evidência para Diálogo e Transparência. As interpretações conceituais estão alinhadas com as definições clássicas de Diálogo (falta de comunicação bidirecional) e Transparência (suspeita de motivos ocultos). O score de risco 3 está bem fundamentado, relacionando a erosão de confiança a um risco moderado, apoiado pelo contexto de baixo engajamento do post. Os metadados (jogo, ID, QIs) são consistentes com o conteúdo e o framework DART. Nenhum erro detetado.

---

### Post Auditado #116: `510142_2865070` — Score: **80/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal para a dimensão Acesso ('Nerf AFK moon mining') não está no corpo do post, mas sim no título. As demais evidências (para Risco) estão corretas. A análise conceitual está alinhada com o framework DART, a pontuação de risco está bem justificada com base no texto, e os metadados (jogo, QIs) parecem consistentes. Dedução de 20 pontos pela imprecisão na citação literal da evidência no corpo.

---

### Post Auditado #117: `3000010_25329840` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todos os critérios de auditoria foram satisfeitos. As evidências literais estão presentes no post original. O enquadramento teórico das dimensões DART está correto: acesso corretamente identificado como assimetria de ferramentas, risco como ameaça à economia, diálogo e transparência ausentes. O score de risco 4 é bem fundamentado, considerando a implicação de bots prevalentes e a importância do loop de jogo. Os metadados são consistentes: jogo, ID, e mapeamento para QI2, QI3 e QI5 estão alinhados com o teor do post.

---

### Post Auditado #118: `504046_2858203` — Score: **95/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A análise não apresenta evidências literais falsas. A classificação de ausência de todas as dimensões DART é conceitualmente correta face ao conteúdo mínimo do post (apenas mensagem de encerramento automático). O score de risco 1 é justificado com base no trust level do autor e encerramento sem incidentes. Os metadados são consistentes. A única fragilidade é a atribuição de 'dimensao_dominante' como 'acesso' quando nenhuma dimensão está presente, o que constitui uma ligeira inconsistência analítica, mas não compromete a exatidão da avaliação.

---

### Post Auditado #119: `3000007_29299248` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** All literal evidence strings are present verbatim in the original post. DART dimensions are correctly interpreted: dialogue is acknowledged but one-way; access is conditioned on participation; risk is identified from economic effects and bugs; transparency is demonstrated through open admission of testing failures and reversal. The risk score of 3 is logically founded on a combination of economic concerns and technical issues and is well justified. Metadata (game, ID, research questions) are coherent and accurately reflect the post.

---

### Post Auditado #120: `3000008_25925540` — Score: **75/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **NÃO** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Evidências literais existem integralmente no post original. A fundamentação do score de risco está lógica e bem justificada, e os metadados (jogo, QIs) são coerentes. Contudo, a dimensão Diálogo é conceitualmente incorreta segundo as definições clássicas do framework DART: a interação observada é uma réplica unilateral num fórum, não constituindo um diálogo ativo entre empresa e consumidor ou cocriação interativa, como exigido por Prahalad & Ramaswamy. A classificação como 'diálogo comunitário' dilui o rigor conceitual. Isso compromete a consistência conceitual global, resultando na dedução de pontos.

---

### Post Auditado #121: `513682_2893021` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais fornecidas para diálogo, risco e transparência estão presentes como substrings exatas no corpo do post original. As definições teóricas aplicadas a cada dimensão DART estão corretas e coerentes com o framework. O score de risco 3 é justificado de forma plausível com base na cautela expressa pelo utilizador e na presença de consequências reais. Os metadados (jogo, ID, mapeamento de QIs) estão consistentes e alinhados com a análise.

---

### Post Auditado #122: `3000006_27255123` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** As evidências literais para risco e transparência estão presentes no post original. As dimensões Diálogo e Acesso foram corretamente identificadas como ausentes. O enquadramento teórico está alinhado com as definições de Diálogo, Acesso, Risco e Transparência. A fundamentação do score de risco 4 é consistente com a linguagem emocional do autor e a perceção de ameaça sistémica, apesar da baixa validação social. Os metadados (jogo, QIs, tipologia) são coerentes com o conteúdo. Nenhum erro foi detetado.

---

### Post Auditado #123: `3000007_29299438` — Score: **75/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **NÃO** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal 'Let’s not assume Blizzard is that competent.' existe no post original. A fundamentação do risco (score 3) é lógica e coerente. Os metadados estão consistentes. No entanto, a dimensão Transparência não se alinha corretamente com as definições clássicas do DART: o post expressa dúvida sobre a competência da Blizzard, e não sobre a abertura ou partilha de informação. O enquadramento como 'falta de transparência' é forçado e enfraquece a consistência conceitual. As restantes dimensões estão corretas.

---

### Post Auditado #124: `487448_2724051` — Score: **80/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal para a dimensão Risco contém uma elipse ('Talking about 'infinite supply' ... unlimited manufacturing jobs per character') que não corresponde a uma frase literal do post original. As restantes evidências literais são exactas. As interpretações conceituais do DART estão alinhadas com as definições, a fundamentação do score de risco (3) é razoável face ao conteúdo, e os metadados são coerentes. Dedução de 20 pontos pela falha de literalidade no Risco.

---

### Post Auditado #125: `514029_2895364` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as frases de evidência literal estão presentes no texto original, sem distorções. As interpretações das dimensões DART (Diálogo, Acesso, Risco, Transparência) estão alinhadas com as definições clássicas — diálogo bidirecional ausente, acesso a ferramentas de sincronização, riscos explícitos de dano ao ecossistema e crítica à falta de transparência da desenvolvedora. O score de risco 5 é plenamente justificado pela gravidade e urgência do discurso, com fundamentação que considera o conteúdo e os metadados contextuais (trust level 0, sem edições). O ID do post, o jogo EVE Online e o mapeamento para as questões de investigação (QI2, QI3, QI4, QI5) são coerentes. Nenhum erro detetado.

---

### Post Auditado #126: `tiktok_dad_1` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais listadas existem exatamente no post original. As interpretações das dimensões DART estão alinhadas com as definições clássicas: diálogo ausente (comunicação unidirecional), acesso a bots, risco de colapso económico e transparência revelada. O score de risco percebido (5) é justificado pela advertência direta de 'economic collapse' no texto, uma ameaça sistémica. Os metadados são coerentes com o jogo e as questões de investigação mapeadas (QI2 a QI5). Nenhuma inconsistência detetada.

---

### Post Auditado #127: `3000008_25927517` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** As evidências literais para as dimensões de risco e transparência estão presentes exatamente no post original. O enquadramento conceitual está correto: Diálogo ausente, Acesso não mencionado, Risco e Transparência identificados com precisão. A fundamentação do score de risco 4 é lógica e considera tanto o conteúdo alarmista quanto os metadados. Os metadados (jogo, ID, mapeamento de QIs) são coerentes e sem discrepâncias.

---

### Post Auditado #128: `511200_2872814` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais estão presentes de forma exata no post original. As interpretações teóricas das dimensões DART estão alinhadas com as definições clássicas: diálogo como interação ativa, acesso como disponibilidade de ferramentas de reporte, risco como mecanismo dissuasor percebido, e transparência como clareza nas regras económicas. O score de risco percebido (2) é coerente com o tom minimizador do autor e está bem fundamentado na argumentação de que os bans e a perda de ativos mitigam os perigos. Os metadados (jogo, ID, QIs) estão consistentes, mapeando corretamente todas as dimensões às questões de investigação. Nenhum erro detetado; a análise é de alta qualidade.

---

### Post Auditado #129: `512435_2883435` — Score: **90/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Evidências literais presentes exatamente no post para Diálogo, Risco e Transparência. A interpretação conceitual de Diálogo é um pouco forçada (monólogo como apelo ao diálogo), mas ainda defensável no contexto de fóruns de EVE Online. Risco e Transparência estão bem enquadrados. A fundamentação do score de risco (4) é lógica e baseada no texto. Metadados coerentes com o post e o mapeamento das QIs. Dedução menor pela elasticidade conceitual em Diálogo.

---

### Post Auditado #130: `3000005_25903097` — Score: **85/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A análise conceitual e a fundamentação do risco estão corretas, e os metadados são coerentes. No entanto, a evidência literal para a dimensão Transparência não é exatamente a que consta no post original: o texto original tem 'You mean that PR tauren  Blizzard tries to feed us? No thanks. I’m not a  eater.', enquanto a análise apresenta 'PR tauren Blizzard tries to feed us? No thanks. I’m not a ** eater.' Essa alteração (omissão do prefixo e substituição do espaço duplo por asteriscos) faz com que a frase não apareça literalmente no corpo do post, invalidando parcialmente o critério de existência literal. Por isso, a pontuação é reduzida para 85.

---

### Post Auditado #131: `1guy1bx_1` — Score: **85/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal para a dimensão 'transparencia' ('your report function is disabled? ... zero consequences. Where is the integrity?') é uma composição de fragmentos não contíguos e não existe como frase literal única no post original, violando o critério de existência literal. As demais dimensões apresentam citações exatas. A consistência conceitual está correta, o score de risco é bem fundamentado e os metadados são coerentes. Pequena inconsistência na literalidade reduz a pontuação.

---

### Post Auditado #132: `3000005_25902774` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** As evidências literais para as dimensões risco e transparência são transcrições exatas do texto do post. As definições conceituais de risco e transparência estão alinhadas com o framework DART, e o acesso e diálogo foram adequadamente assinalados como ausentes. O score de risco de 3 é justificado pela descrição do post como reconhecimento de um risco estrutural moderado, complementado por metadados contextuais. Os metadados de jogo, ID, QIs e outros parâmetros são consistentes. Nenhum erro detetado.

---

### Post Auditado #133: `513682_2895280` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais citadas constam exatamente no post original. As interpretações de Diálogo, Acesso, Risco e Transparência estão alinhadas com as definições clássicas do framework DART. O score de risco percebido (4) está bem fundamentado na expressão do autor sobre dano colateral a jogadores legítimos. Os metadados (jogo, QIs) são consistentes com o post.

---

### Post Auditado #134: `509972_2863398` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais listadas existem textualmente no post original. A dimensão Risco está teoricamente bem enquadrada (ameaça de ganking como risco de jogo e risco económico de recursos sem valor), consistente com as definições clássicas de DART. A fundamentação do score 2 utiliza corretamente metadados (trust level, likes) e texto do post, justificando um risco moderado. Metadados (jogo, ID, QIs) são coerentes. Nenhuma inconformidade detetada.

---

### Post Auditado #135: `3000005_25903071` — Score: **95/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as frases de evidência literal existem exatamente no corpo do post. As definições de Diálogo, Acesso, Risco e Transparência estão aplicadas corretamente ao contexto de bots em World of Warcraft. O score de risco 3 está justificado com base no tom, trust level e ausência de likes, sendo uma interpretação plausível. O jogo está correto, o ID é consistente em formato, e as QIs mapeadas correspondem às dimensões identificadas. Não se encontraram erros.

---

### Post Auditado #136: `509843_2862442` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as frases de evidência literal listadas nas dimensões Diálogo, Acesso, Risco e Transparência foram encontradas textualmente no post original. A aplicação dos conceitos DART está correta e alinhada com as definições de Prahalad & Ramaswamy (2004), refletindo adequadamente diálogo, acesso, risco e transparência. A fundamentação do score de risco (4/5) é coerente com o texto, apoiada na identificação explícita de impacto económico elevado e no nível de confiança do autor. Os metadados (jogo, ID e mapeamento de QIs) são consistentes com o conteúdo e a análise. Nenhuma desconformidade detetada.

---

### Post Auditado #137: `511102_2873144` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais citadas (diálogo, acesso, risco, transparência) foram encontradas de forma exata no post original. Os conceitos do framework DART foram aplicados corretamente, com interpretações alinhadas às definições clássicas. O score de risco percebido (4) está bem justificado com base na menção de perdas financeiras e ameaças econômicas e sociais. Os metadados do jogo (EVE Online) e o mapeamento completo das cinco questões de investigação são consistentes. Nenhum erro identificado.

---

### Post Auditado #138: `3000006_27255816` — Score: **95/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal utilizada (I have been farming in EPL … wel this is your first problem) combina duas frases separadas do post original com uma elipse, mas ambas as expressões-chave estão textualmente presentes na postagem, validando a existência da evidência. A análise conceitual enquadra corretamente apenas a dimensão Risco, consistente com as definições clássicas do DART, e as demais dimensões são adequadamente assinaladas como ausentes. A fundamentação do score de risco (2) integra o tom sarcástico, os metadados (likes, trust level, edits) e o contexto do título, oferecendo uma justificação lógica e proporcional ao conteúdo. Os metadados (jogo, ID, QIs) estão coerentes. Pequena ressalva pela concatenação não literal, mas sem prejuízo da qualidade geral.

---

### Post Auditado #139: `513682_2895541` — Score: **50/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **NÃO** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal para Transparência não existe como sequência contígua no post: 'You can see the timings in log. So it is easy to see if that ganker uses input broadcast of not.' não está presente textualmente; o post intercala 'And you don’t even need to be target...' entre as frases. Consistência conceitual falha: o enquadramento de Diálogo como 'comunicação de dupla via onde um jogador desafia a narrativa dominante' não atende à definição DART, que exige interação empresa-consumidor; o diálogo aqui é apenas entre jogadores. Fundamentação do score de risco (4) é válida e baseada no texto. Metadados (jogo, ID, QIs) estão coerentes.

---

### Post Auditado #140: `512885_2886412` — Score: **75/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal para a dimensão Risco é 'Shuttle Smart-bombing Is Anti-Gameplay, Not PvP', que corresponde ao título do post, mas não está presente no corpo da mensagem original. As outras evidências (diálogo e acesso) foram corretamente extraídas do corpo. A consistência conceitual das dimensões DART está adequada, o score de risco é bem fundamentado e os metadados estão coerentes. A falha na literalidade da evidência de Risco reduz a qualidade da análise.

---

### Post Auditado #141: `3000011_23370925` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** As evidências literais para as dimensões 'acesso' e 'risco' estão presentes de forma exata no corpo do post, incluindo os erros tipográficos originais. O enquadramento teórico está correto: 'acesso' reflete o uso de ferramentas de personalização (macros), 'risco' capta a defesa contra acusações de batota, e as dimensões ausentes ('diálogo', 'transparência') são justificadas. A fundamentação do score de risco percebido (2) é consistente com o tom defensivo do post, o baixo engajamento e o contexto da thread. Os metadados (jogo, QIs, tipologia) são coerentes com o conteúdo. Não foram identificados erros.

---

### Post Auditado #142: `511102_2873163` — Score: **75/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **NÃO** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal existe para as dimensões Acesso e Risco, estando as frases citadas presentes no post original. A fundamentação do score de risco é válida, baseando-se na linguagem apocalíptica e na argumentação do autor. Os metadados (jogo, ID, mapeamento das QIs) são coerentes. No entanto, a análise apresenta inconsistência conceitual ao classificar o Diálogo como ausente. O post consiste numa discussão entre jogadores, o que se enquadra na definição de Diálogo do framework DART (interação consumidor-consumidor facilitada pela plataforma). A justificação apresentada ('não é um diálogo com developers ou IA') é demasiado restritiva, ferindo a correta aplicação do modelo.

---

### Post Auditado #143: `509843_2862478` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais listadas (diálogo e risco) estão presentes de forma exata no corpo do post original. O enquadramento teórico de diálogo e risco está correto segundo as definições clássicas do DART. O score de risco 2 está bem fundamentado, coerente com o tom propositivo e moderado do post. Os metadados – jogo 'EVE Online', ID '509843_2862478' e mapeamento das QIs (QI1, QI3, QI5) – são consistentes entre si e com o conteúdo analisado.

---

### Post Auditado #144: `514029_2896826` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais listadas para Diálogo e Risco ('I hope you understand the significant difference, botters can be AFK and use 3rd party software.') existem textualmente no corpo do post original. O enquadramento teórico das dimensões DART está correto: o Diálogo manifesta-se na clarificação interativa; o Risco decorre do receio implícito de sanção por má classificação; Acesso e Transparência estão corretamente assinalados como ausentes. A fundamentação do score de risco 3 é lógica, baseando-se na moderação do teor do post e no contexto do tópico, sem alarme explícito mas com ameaça à integridade da conta. Os metadados são coerentes: jogo 'EVE Online', post_id plausível e mapeamento das QI1, QI3 e QI5 alinhado com as dimensões identificadas. Nenhum erro detetado.

---

### Post Auditado #145: `3000000_22980572` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todos os critérios foram satisfeitos. As evidências literais citadas existem exatamente no post original. O enquadramento das dimensões DART (Diálogo, Acesso, Risco, Transparência) está correto segundo as definições clássicas. O score de risco percebido (3) é bem fundamentado, considerando o cenário hipotético extremo mas temporário descrito pelo autor, e a argumentação é lógica. Os metadados estão consistentes: jogo, ID (conforme fornecido) e mapeamento das QIs (QI3 e QI5) são adequados ao conteúdo do post.

---

### Post Auditado #146: `514029_2895257` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todos os critérios foram satisfeitos. As evidências literais (título e fragmentos) aparecem de forma exata no post original. As interpretações das dimensões DART (Diálogo, Acesso, Risco e Transparência) estão conceptualmente corretas. O score de risco 5 está justificado de forma lógica considerando a gravidade da alegação, a experiência do autor e o contexto do jogo. Os metadados (ID, jogo, QIs) são totalmente coerentes com o conteúdo e a tipologia atribuída.

---

### Post Auditado #147: `509972_2863255` — Score: **95/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as verificações são positivas. A evidência literal listada para 'risco' está presente no post original (incluindo o trecho censurado). O enquadramento conceitual DART está correto: Diálogo e Transparência ausentes, Risco presente de forma fundamentada. A justificação do score de risco 3 é lógica e apoia-se nos metadados (trust level 3, 0 likes) e no tom comedido do autor. Metadados como jogo, questões de investigação e tipologia são coerentes. Pequena ressalva apenas pela palavra censurada, que não compromete a análise, resultando em score 95.

---

### Post Auditado #148: `513682_2897072` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as frases de evidência literal estão presentes de forma exata no post original. As interpretações teóricas estão alinhadas com as definições do framework DART: diálogo como engajamento crítico, acesso como ferramentas de multiboxing, risco como incentivo ao cheating, e transparência como questionamento da lógica do desenvolvedor. O score de risco 4 é bem fundamentado com base no texto e nos metadados (edições, trust level). Os metadados (jogo, ID, QIs) estão consistentes e mapeiam corretamente todas as dimensões. Nenhum erro identificado.

---

### Post Auditado #149: `487448_2723498` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todas as evidências literais citadas existem de forma precisa no post original, incluindo 'Don’t be silly...', 'If I lose an Eagle...' e 'If you don’t grasp that...'. As interpretações conceituais de diálogo, acesso, risco e transparência estão alinhadas com as definições clássicas do framework DART, embora a aplicação de transparência possa ser ligeiramente indireta, ainda é teoricamente válida. O score de risco percebido 3 é bem fundamentado, apoiando-se no argumento de normalização do risco, no trust level do autor e na ausência de validação social. Os metadados são consistentes: jogo, IDs e as questões de investigação (QI1, QI3, QI4, QI5) refletem corretamente as dimensões identificadas. Não foram detetados erros, a análise é de alta qualidade.

---

### Post Auditado #150: `3000008_25929808` — Score: **100/100**
* **Critérios:** Evidência Literal: **SIM** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** Todos os critérios são satisfeitos. A frase 'The economy is NOT fine.' é citada literalmente como evidência de risco. O enquadramento teórico do risco como perceção de ameaça à integridade/experiência económica do jogador é compatível com as definições clássicas do DART (risco do consumidor na cocriação). O score 4 está bem fundamentado com base nos preços inflacionados e no tom urgente, e os metadados (jogo, ID, QIs) são coerentes.

---

### Post Auditado #151: `509972_2863383` — Score: **75/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **SIM** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal listada para 'Acesso' ('wondering how many "mega multis" will be heading to Exordium to avoid ganks') e para 'Risco' (composta por fragmentos do título e do corpo) não consta de forma literal no corpo do post original, que se limita a: 'This new new Eden now known as the “Exotic Mining Garden of Eden” Has many pilots wondering about restarting a new pilot n secret'. As demais dimensões (conceitual, risco e metadados) estão corretas e coerentes.

---

### Post Auditado #152: `2211172_28348048` — Score: **0/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **NÃO** | Risco Válido: **NÃO** | Metadados Coerentes: **NÃO**
* **Justificação do Auditor Académico:** Falha ao executar auditoria: Expecting value: line 1 column 1 (char 0)

---

### Post Auditado #153: `514029_2896813` — Score: **40/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **NÃO** | Risco Válido: **SIM** | Metadados Coerentes: **SIM**
* **Justificação do Auditor Académico:** A evidência literal de 'acesso' está truncada, omitindo '(since [ID_ANONYMIZED])', pelo que não corresponde exatamente ao texto do post. As dimensões DART 'Acesso' e 'Risco' estão mal aplicadas: o conceito clássico de acesso refere-se à democratização de informação e ferramentas pela empresa, não à prática de multiboxing; risco, no modelo DART, diz respeito aos riscos assumidos pelo consumidor no processo de cocriação, e não ao risco sistémico percebido na economia do jogo. Isso compromete a consistência conceitual. A fundamentação do score de risco percebido é, contudo, lógica e consistente com o discurso do post. Os metadados (ID, jogo, QIs) estão coerentes.

---

### Post Auditado #154: `xaonz7_6` — Score: **0/100**
* **Critérios:** Evidência Literal: **NÃO** | Conceito DART: **NÃO** | Risco Válido: **NÃO** | Metadados Coerentes: **NÃO**
* **Justificação do Auditor Académico:** Falha ao executar auditoria: Unterminated string starting at: line 7 column 29 (char 197)

---
