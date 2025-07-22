def calcular_viga(datos):
    rc = float(datos['rc'])
    fy = float(datos['fy'])
    nombre = datos['nombre']
    ubicacion = datos['ubicacion']
    fecha = datos['fecha']
    l = float(datos['l'])
    ce = float(datos['ce'])
    cd = float(datos['cd'])
    n = float(datos['n'])
    q1 = float(datos['q1'])
    q2 = float(datos['q2'])
    ns = int(datos['ns'])
    k = int(datos['k'])
    j = int(datos['j'])
    p = 1.815
    a = 4.267
    w = 18.2
    ci = 15.24 / (l + 38.11) + 1
    if ci > 1.3:
        ci = 1.3
    c = ci * cd * ce
    rr = 100000

    m1 = []
    m2 = []
    m3 = []

    x = [float(val) for val in datos['x']]
#    x = datos['x']
    for i in range(ns):
        m1.append(0.5 * q1 * x[i] * (l - x[i]))
        m2.append(0.5 * q2 * x[i] * (l - x[i]))
        m31 = p * (9 * (l - x[i]) - 6 * a) * x[i] / l
        m3.append(m31)
        m1[i] *= rr
        m2[i] *= rr
        m3[i] *= rr

    resultados = {
        'nombre': nombre,
        'ubicacion': ubicacion,
        'fecha': fecha,
        'rc': rc,
        'fy': fy,
        'm1': m1,
        'm2': m2,
        'm3': m3,
    }
    return resultados
