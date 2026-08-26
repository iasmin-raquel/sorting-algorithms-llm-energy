"""
Gera um resumo tabular (Rodada 1, Rodada 2, ..., Total, Média) a partir
do CSV bruto de emissões do CodeCarbon acumulado por um dos scripts
medir_*.py, pronto para colar na planilha do TCC.

Total (TE / TCO2 / TEC) = soma das rodadas.
Média (ME / CO2eq/s) = média das rodadas.

TEC (Total Energy Consumed, kWh) = soma de energy_consumed (cpu+gpu+ram),
métrica de energia separada de TCO2/CO2eq-s (RQ3 pede as duas coisas:
"energy consumption and CO2 emissions").

Uso:
  python3 ollama/scripts/metricas-codigo/resumo_medicoes.py <nome-da-pasta-do-combo>
  ex: python3 ollama/scripts/metricas-codigo/resumo_medicoes.py mandelbrot_qwen2.5_cot_0_cpp

Lê ollama/resultados/<combo>/emissoes_<problema>.csv e escreve
ollama/resultados/<combo>/resumo_<problema>.csv ao lado.
"""
import os
import sys
import pandas as pd


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    combo = sys.argv[1]
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # ollama/
    resultados_dir = os.path.join(base_dir, "resultados", combo)

    if not os.path.isdir(resultados_dir):
        print(f"ERRO: pasta não encontrada: {resultados_dir}")
        sys.exit(1)

    candidatos = [f for f in os.listdir(resultados_dir) if f.startswith("emissoes_") and f.endswith(".csv")]
    if len(candidatos) != 1:
        print(f"ERRO: esperava 1 arquivo emissoes_*.csv em {resultados_dir}, achei {len(candidatos)}: {candidatos}")
        sys.exit(1)

    csv_path = os.path.join(resultados_dir, candidatos[0])
    df = pd.read_csv(csv_path)

    projetos = df["project_name"].unique()
    if len(projetos) > 1:
        mais_recente = df.iloc[-1]["project_name"]
        print(f"AVISO: {len(projetos)} project_name diferentes em {candidatos[0]}; usando só '{mais_recente}'.")
        df = df[df["project_name"] == mais_recente]

    df = df.sort_values("timestamp").reset_index(drop=True)

    tabela = pd.DataFrame({
        "Rodada": range(1, len(df) + 1),
        "Duração (s)": df["duration"],
        "Energia (kWh)": df["energy_consumed"],
        "CO2 (g)": df["emissions"] * 1000,
        "CO2eq/s (g/s)": df["emissions_rate"] * 1000,
    })

    total = pd.DataFrame([{
        "Rodada": "Total (TE / TEC / TCO2)",
        "Duração (s)": tabela["Duração (s)"].sum(),
        "Energia (kWh)": tabela["Energia (kWh)"].sum(),
        "CO2 (g)": tabela["CO2 (g)"].sum(),
        "CO2eq/s (g/s)": "",
    }])
    media = pd.DataFrame([{
        "Rodada": "Média (ME)",
        "Duração (s)": tabela["Duração (s)"].mean(),
        "Energia (kWh)": tabela["Energia (kWh)"].mean(),
        "CO2 (g)": tabela["CO2 (g)"].mean(),
        "CO2eq/s (g/s)": tabela["CO2eq/s (g/s)"].mean(),
    }])

    resultado = pd.concat([tabela, total, media], ignore_index=True)
    print(f"=== {projetos[-1] if len(projetos) > 1 else projetos[0]} ({len(tabela)} rodadas) ===")
    print(resultado.to_string(index=False))

    saida = os.path.join(resultados_dir, f"resumo_{candidatos[0].split('emissoes_', 1)[1]}")
    resultado.to_csv(saida, index=False)
    print(f"\nResumo salvo em: {os.path.relpath(saida, base_dir)}")


if __name__ == "__main__":
    main()
