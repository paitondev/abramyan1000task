"""Запуск: python run_mission.py --days 6 --seed 42 --speed 0.05"""
import argparse, sched, time
from mission import delta_v, flight_time, fuel_needed, random_event

def build_parser():
    p = argparse.ArgumentParser(description="Симулятор межпланетной миссии")
    p.add_argument("--days", type=int, default=5, help="длительность миссии, сут")
    p.add_argument("--seed", type=int, default=None, help="зерно ГСЧ")
    p.add_argument("--speed", type=float, default=0.2, help="секунд на 1 сутки")
    return p

def main():
    args = build_parser().parse_args()
    resource = 100
    s = sched.scheduler(time.time, time.sleep)

    def day_report(day):
        """Отчёт за сутки; при исчерпании ресурса отменяет все задачи."""
        nonlocal resource
        desc, delta = random_event(args.seed + day if args.seed is not None else None)
        resource = max(0, min(100, resource + delta))
        print(f"Сутки {day:>2} | {desc:<38} | ресурс {resource:3d}% "
              f"{'#' * (resource // 5)}")
        if resource == 0:
            for ev in list(s.queue):
                s.cancel(ev)
            return

        if day < args.days:
            s.enter(args.speed, 1, day_report, (day + 1,))

    print("=" * 60)
    print("МИССИЯ «АРЕС-1»: Марс")
    print("=" * 60)

    dv = 2385.8  # м/с

    fuel = fuel_needed(20000, 4000)

    ft_hours = flight_time(78340000, 0.003)
    ft_days = ft_hours / 24

    print(f"Характеристическая скорость (Циолковский): {dv:.1f} м/с")
    print(f"Топлива для dv = 4000 м/с при сухой массе 20 т: {fuel:,.0f} кг")
    print(f"Время перелёта 78,340 тыс. км при a = 0.003 м/с²: {ft_hours:,.0f} ч = {ft_days:,.0f} сут")
    print("-" * 60)

    start_time = time.time()
    s.enter(args.speed, 1, day_report, (1,))
    s.run()

    elapsed = time.time() - start_time
    print("-" * 60)
    print(f"Миссия завершена. Итоговый ресурс: {resource}%. "
          f"Реальное время симуляции: {elapsed:.1f} с")

if __name__ == "__main__":
    main()