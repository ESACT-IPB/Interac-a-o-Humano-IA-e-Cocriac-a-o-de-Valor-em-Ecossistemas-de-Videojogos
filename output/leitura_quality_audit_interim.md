# Auditoria de Qualidade Inicial (Fase Intercalar / Protótipo)

> [!NOTE]
> Este documento reflete os dados do ficheiro de teste histórico `data/interim/quality_audit.json`, gerado durante os primeiros testes de prototipagem da pipeline (1 de julho de 2026). Para os resultados de produção completos e ativos, consulte `output/leitura_quality_audit_results.md`.

---

## 1. Registos Auditados no Protótipo (6 posts de teste)

| # | ID Auditado | Correspondência Literal | Consistência Score | Tipo Apropriado | QIs Corretas | Aprovado |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | `post_0011` | SIM | SIM | SIM | SIM | **SIM** |
| 2 | `post_0027` | SIM | SIM | SIM | SIM | **SIM** |
| 3 | `post_0026` | SIM | SIM | NÃO | SIM | NÃO |
| 4 | `post_0043` | SIM | SIM | SIM | SIM | **SIM** |
| 5 | `post_0023` | SIM | SIM | SIM | SIM | **SIM** |
| 6 | `post_0008` | SIM | SIM | SIM | SIM | **SIM** |

## 2. Notas Detalhadas de Cada Auditoria

### Teste #1: `post_0011`
* **Estado de Aceitação:** Aprovado
* **Notas da Auditoria:** All checks passed: quote found verbatim, scores consistent with evidence, parasitic type fits the AI exploitation narrative, and research questions align with the post content.

### Teste #2: `post_0027`
* **Estado de Aceitação:** Aprovado
* **Notas da Auditoria:** The quote appears verbatim in the post. Scores appropriately reflect the public access, moderate risk of platform moderation, low transparency of pseudonymous identity, and minimal dialogue in a single complaint post. Parasitic co-creation accurately describes gold buyers exploiting GDKP runs. Research question mapping fits the themes of monetization and fairness.

### Teste #3: `post_0026`
* **Estado de Aceitação:** Rejeitado
* **Notas da Auditoria:** Quote evidence is verbatim and scores are plausible, but the co-creation type is misclassified: the WeakAura unilaterally dictates assignments without reciprocal input, making it asymmetric rather than symmetric.

### Teste #4: `post_0043`
* **Estado de Aceitação:** Aprovado
* **Notas da Auditoria:** The quote is a direct match, scores appropriately reflect the post's emphasis on essential addons (Access 5) and minimal dialogue, the asymmetric type correctly captures the tension with automation, and the research questions align with the post's theme.

### Teste #5: `post_0023`
* **Estado de Aceitação:** Aprovado
* **Notas da Auditoria:** Quote evidence matches post body exactly. DART scores align with the post content, especially Access and Risk. The co-creation type 'parasitic' is justified. Research question mapping appears correct. Minor: Transparency score only weakly indicated by the evidence, but the third sentence regarding Blizzard's unfulfilled promise supports low transparency, so it is acceptable.

### Teste #6: `post_0008`
* **Estado de Aceitação:** Aprovado
* **Notas da Auditoria:** The quote_evidence appears verbatim in the post body. DART scores are consistent with the player's description of low dialogue, moderate access, high perceived risk, and limited transparency. Asymmetric co-creation correctly reflects the unequal value and exploitation. Research question mapping is appropriate for a post focused on agency loss due to automation.
