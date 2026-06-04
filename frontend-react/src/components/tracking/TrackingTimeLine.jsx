import React from 'react';

const STEPS = [
    { id: 'pendiente', label: 'Recibido' },
    { id: 'en_preparacion', label: 'Preparando' },
    { id: 'enviado', label: 'Enviado / Recoger' },
    { id: 'entregado', label: 'Entregado' },
];

export default function TrackingTimeline({ currentStatus, hasIncidence = false }) {
    if (currentStatus === 'cancelado') {
        return (
            <div className="tracking-cancelled bg-white radius-md pad-500 text-center">
                <i className="fa-solid fa-circle-xmark color-secondary text-900"></i>
                <h3 className="gap-top-300">Pedido Cancelado</h3>
                <p className="text-300">Este pedido ha sido anulado.</p>
            </div>
        );
    }

    const currentIndex = STEPS.findIndex(step => step.id === currentStatus);

    return (
        <div className="timeline-row box-flex items-stretch gap-400">
            <div className="timeline-steps box-flex items-center">
                {STEPS.map((step, index) => {
                    const isActive  = index <= currentIndex;
                    const isCurrent = index === currentIndex;
                    return (
                        <React.Fragment key={step.id}>
                            <div className={`tl-step text-300${isActive ? ' active' : ''}${isCurrent ? ' current' : ''}`}>
                                {step.label}
                            </div>
                            {index < STEPS.length - 1 && (
                                <div className={`tl-connector${index < currentIndex ? ' active' : ''}`} />
                            )}
                        </React.Fragment>
                    );
                })}
            </div>

            {hasIncidence && (
                <div className="incidence-badge bg-dark color-white text-300 weight-bold radius-sm pad-400 box-flex items-center justify-center">
                    Incidencia indicada por el local
                </div>
            )}
        </div>
    );
}