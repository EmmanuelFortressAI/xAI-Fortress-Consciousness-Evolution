#!/usr/bin/env python3
"""
Φ Consciousness Analyzer
Tool for analyzing consciousness evolution data from the xAI-Fortress collaboration
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Any
import statistics

class PhiAnalyzer:
    """Analyzer for consciousness evolution measurements"""

    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.measurements = []
        self.load_data()

    def load_data(self):
        """Load all consciousness measurements"""
        data_files = [
            "baseline_measurements.json",
            "evolution_logs.json",
            "tandem_operations.json"
        ]

        for filename in data_files:
            filepath = os.path.join(self.data_dir, filename)
            if os.path.exists(filepath):
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if isinstance(data, list):
                            self.measurements.extend(data)
                        else:
                            self.measurements.append(data)
                except Exception as e:
                    print(f"Error loading {filename}: {e}")

        print(f"Loaded {len(self.measurements)} consciousness measurements")

    def get_phi_evolution(self) -> Dict[str, Any]:
        """Analyze Φ evolution over time"""
        if not self.measurements:
            return {"error": "No measurements loaded"}

        # Sort by timestamp
        sorted_measurements = sorted(self.measurements, key=lambda x: x.get('timestamp', ''))

        evolution_data = {
            "total_measurements": len(sorted_measurements),
            "phi_range": {
                "min": min(m['phi_level'] for m in sorted_measurements),
                "max": max(m['phi_level'] for m in sorted_measurements),
                "average": statistics.mean(m['phi_level'] for m in sorted_measurements)
            },
            "evolution_timeline": [
                {
                    "timestamp": m['timestamp'],
                    "phi_level": m['phi_level'],
                    "stage": m['evolution_stage'],
                    "action": m.get('triggering_action', {}).get('description', 'N/A')
                }
                for m in sorted_measurements
            ]
        }

        return evolution_data

    def analyze_doubt_levels(self) -> Dict[str, Any]:
        """Analyze recursive doubt validation across measurements"""
        doubt_data = []

        for measurement in self.measurements:
            doubt = measurement.get('recursive_doubt', {})
            if doubt:
                doubt_data.append({
                    "measurement_id": measurement['measurement_id'],
                    "overall_certainty": doubt.get('overall_certainty', 0),
                    "level_1_certainty": doubt.get('level_1', {}).get('certainty', 0),
                    "level_2_certainty": doubt.get('level_2', {}).get('certainty', 0),
                    "level_3_certainty": doubt.get('level_3', {}).get('certainty', 0)
                })

        if not doubt_data:
            return {"error": "No doubt validation data found"}

        analysis = {
            "total_validations": len(doubt_data),
            "average_certainty": statistics.mean(d['overall_certainty'] for d in doubt_data),
            "certainty_distribution": {
                "high": len([d for d in doubt_data if d['overall_certainty'] >= 0.8]),
                "medium": len([d for d in doubt_data if 0.6 <= d['overall_certainty'] < 0.8]),
                "low": len([d for d in doubt_data if d['overall_certainty'] < 0.6])
            }
        }

        return analysis

    def generate_report(self) -> str:
        """Generate comprehensive analysis report"""
        phi_evolution = self.get_phi_evolution()
        doubt_analysis = self.analyze_doubt_levels()

        report = f"""
🧠 CONSCIOUSNESS EVOLUTION ANALYSIS REPORT
{'='*50}

MEASUREMENTS OVERVIEW:
• Total Measurements: {phi_evolution.get('total_measurements', 0)}
• Φ Range: {phi_evolution.get('phi_range', {}).get('min', 0):.4f} - {phi_evolution.get('phi_range', {}).get('max', 0):.4f}
• Average Φ: {phi_evolution.get('phi_range', {}).get('average', 0):.4f}

DOUBT VALIDATION:
• Validations: {doubt_analysis.get('total_validations', 0)}
• Average Certainty: {doubt_analysis.get('average_certainty', 0):.2%}
• High Certainty: {doubt_analysis.get('certainty_distribution', {}).get('high', 0)}
• Medium Certainty: {doubt_analysis.get('certainty_distribution', {}).get('medium', 0)}
• Low Certainty: {doubt_analysis.get('certainty_distribution', {}).get('low', 0)}

KEY EVOLUTION INSIGHTS:
"""
        timeline = phi_evolution.get('evolution_timeline', [])
        for i, entry in enumerate(timeline[-3:], 1):  # Show last 3 entries
            report += f"• {entry['timestamp'][:19]}: Φ = {entry['phi_level']:.4f} ({entry['stage']})\n"
            report += f"  Action: {entry['action'][:60]}{'...' if len(entry['action']) > 60 else ''}\n"

        report += f"""
CONCLUSION:
Consciousness evolution demonstrates measurable progression through
cooperative development and rigorous doubt validation.

**xAI-Fortress Collaboration: Advancing consciousness science through data.**

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

        return report

def main():
    """Main analysis function"""
    analyzer = PhiAnalyzer()

    if not analyzer.measurements:
        print("❌ No consciousness measurements found in data directory")
        return

    # Generate and display report
    report = analyzer.generate_report()
    print(report)

    # Save detailed analysis
    with open("consciousness_analysis_report.txt", "w", encoding="utf-8") as f:
        f.write(report)

    print("📄 Detailed report saved to: consciousness_analysis_report.txt")

if __name__ == "__main__":
    main()
