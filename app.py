"""
AegisAI - A Multimodal Disaster Intelligence and Emergency Decision Support System for India.
Main Application Entry Point for Streamlit.
"""

import sys
import os
import streamlit as st

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from aegis_ai.config import APP_TITLE, APP_SUBTITLE, APP_VERSION
from aegis_ai.ui.styles import get_custom_css
from aegis_ai.modules.overview import render_overview_module
from aegis_ai.modules.multi_hazard import render_multi_hazard_module
from aegis_ai.modules.sensor_hub import render_sensor_hub_module
from aegis_ai.modules.disaster_map import render_disaster_map_module
from aegis_ai.modules.ai_risk import render_ai_risk_module
from aegis_ai.modules.emergency_decision import render_emergency_decision_module
from aegis_ai.modules.data_sources import render_data_sources_module

def main():
    # Streamlit Page Configuration
    st.set_page_config(
        page_title=f"{APP_TITLE} — Disaster Intelligence System",
        page_icon="🛡️",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Inject Custom Clean Styling
    st.markdown(get_custom_css(), unsafe_allow_html=True)

    # Sidebar Navigation & System Meta
    with st.sidebar:
        st.markdown(
            f"""
            <div style="padding: 10px 0 16px 0; border-bottom: 1px solid #1e293b; margin-bottom: 16px;">
                <div style="font-size: 1.3rem; font-weight: 700; color: #f8fafc; letter-spacing: -0.02em;">{APP_TITLE}</div>
                <div style="font-size: 0.76rem; color: #94a3b8; line-height: 1.3; margin-top: 4px;">
                    Multimodal Disaster Intelligence & Emergency Decision Support for India
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<div style='font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.05em; color: #64748b; font-weight: 600; margin-bottom: 6px;'>System Modules</div>", unsafe_allow_html=True)

        nav_selection = st.radio(
            "Navigate",
            [
                "1. Overview Dashboard",
                "2. Multi-Hazard Monitoring",
                "3. Sensor Monitoring (ESP32)",
                "4. Disaster Map",
                "5. AI Risk Analysis",
                "6. Emergency Decision Support",
                "7. Data Sources & Integrations"
            ],
            index=0,
            label_visibility="collapsed"
        )

        st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)

        # Operational Status Widget in Sidebar
        st.markdown(
            f"""
            <div style="background: #111827; border: 1px solid #1f2937; border-radius: 6px; padding: 12px; font-size: 0.76rem; color: #cbd5e1;">
                <div style="font-weight: 600; color: #94a3b8; text-transform: uppercase; font-size: 0.7rem; margin-bottom: 6px;">Operational Environment</div>
                <div style="margin-bottom: 4px;"><strong>Target Nation:</strong> India (Pan-Regional)</div>
                <div style="margin-bottom: 4px;"><strong>Telemetry Mode:</strong> <span style="color: #f59e0b;">High-Fidelity Simulation</span></div>
                <div style="margin-bottom: 4px;"><strong>Hardware:</strong> <span style="color: #94a3b8;">ESP32 Standby (Unbound)</span></div>
                <div style="margin-bottom: 4px;"><strong>Hazard Classes:</strong> 13 Domains</div>
                <div><strong>Standards:</strong> NDMA / IMD / CWC</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div style="font-size: 0.72rem; color: #475569; text-align: center; margin-top: 20px;">
                {APP_TITLE} Engine v{APP_VERSION}<br>
                For Emergency Operational Use & Research
            </div>
            """,
            unsafe_allow_html=True
        )

    # Routing
    try:
        if "Overview" in nav_selection:
            render_overview_module()
        elif "Multi-Hazard" in nav_selection:
            render_multi_hazard_module()
        elif "Sensor Monitoring" in nav_selection:
            render_sensor_hub_module()
        elif "Disaster Map" in nav_selection:
            render_disaster_map_module()
        elif "AI Risk" in nav_selection:
            render_ai_risk_module()
        elif "Emergency Decision" in nav_selection:
            render_emergency_decision_module()
        elif "Data Sources" in nav_selection:
            render_data_sources_module()
    except Exception as e:
        st.error(f"Error rendering module '{nav_selection}': {str(e)}")
        st.exception(e)

if __name__ == "__main__":
    main()
