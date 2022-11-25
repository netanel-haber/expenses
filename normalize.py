import pandas as pd
import hebrew_category as hc
import category as ca
import column as cl
import executor as ex

straight_forward_replacements = {
    hcat: cat
    for cat, hcats in (
        {
            ca.RENT: [
                hc.CHECK,
                hc.RENT_PAYBACK,
                hc.RENT_PAYBACK_2,
                hc.STANDING_ORDER,
                hc.MIZRAHI_RENT,
                hc.ONE_TIME_ORDER,
            ],
            ca.SALARY: [hc.SALARY, hc.SALARY_NET, hc.SALARY_3, hc.UNEMPLOYMENT],
            ca.CREDIT_CARD: [hc.CREDIT_CARD, hc.ATM, hc.BIT, hc.FOREX],
            ca.DEBIT_CARD: [hc.DIRECT, hc.DIRECT_BATCHED],
            ca.IB: [hc.IB],
            ca.BANK: [hc.BANK, hc.REBATE],
            ca.MISC: [hc.CRAP, hc.REBATE],
            ca.ARMY_REBATE: [hc.ARMY_REBATE],
        }
    ).items()
    for hcat in hcats
}


def replace_action_when_executor(df, executor: str, to_category: str):
    df.loc[df[cl.EXECUTOR] == executor, cl.ACTION] = to_category


def filter_out_categories(df: pd.DataFrame, cas: set[str]) -> pd.DataFrame:
    return df[~df[cl.ACTION].isin(cas)]


def normalize(df: pd.DataFrame) -> pd.DataFrame:
    replace_action_when_executor(df, ex.IB, ca.IB)
    replace_action_when_executor(df, ex.PARENTS, ca.INHERITANCE)
    replace_action_when_executor(df, ex.YAHEL_MEDITATION, ca.MEDITATION)
    replace_action_when_executor(df, ex.BUILDING_TAX, ca.BUILDING_TAX)
    df = df.replace(straight_forward_replacements)

    unaccounted_for_categories = df[~df[cl.ACTION].isin(ca.__dict__.values())]
    assert (
        unaccounted_for_categories.empty
    ), f"{unaccounted_for_categories[cl.ACTION]} - all actions must be registered in categories module."

    df = filter_out_categories(
        df, {ca.IB, ca.INHERITANCE, ca.ARMY_REBATE, ca.SALARY, ca.MISC}
    )

    df[cl.DATE] = pd.to_datetime(df[cl.DATE], dayfirst=True)
    df[cl.BALANCE] = pd.to_numeric(df[cl.BALANCE])
    df[cl.MINUS] = pd.to_numeric(df[cl.MINUS]).fillna(0)
    df[cl.PLUS] = pd.to_numeric(df[cl.PLUS]).fillna(0)
    df[cl.DIFF] = df[cl.MINUS] - df[cl.PLUS]

    return df
