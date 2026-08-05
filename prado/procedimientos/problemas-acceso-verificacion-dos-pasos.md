---
type: Procedure
title: Problemas de acceso o verificación en dos pasos
description: Procedimiento para atender incidencias relacionadas con la configuración, el bloqueo y los códigos de la doble autenticación de PRADO.
service: PRADO
audience: personal-cau
status: draft
owner: FOL
usual_ticket_category: Acceso
language: es
confidentiality: uso-interno
timestamp: 2026-08-03T23:42:04Z
review_date: 2026-11-05
last_reviewed: 2026-08-03
tags:
  - prado
  - acceso
  - 2fa
  - doble-autenticacion
  - codigo-seguridad
  - app-autenticacion
---

# Problemas de acceso o verificación en dos pasos

## Objetivo

Determinar por qué una persona no puede completar la verificación en dos pasos —2FA— de PRADO y establecer si procede:

- corregir el uso del código;
- revisar la hora del dispositivo;
- completar nuevamente la configuración;
- utilizar el correo electrónico como alternativa;
- restablecer el proceso de doble autenticación;
- o comprobar por separado PRADO Grado y PRADO Posgrado.

## Qué es la doble autenticación

La doble autenticación es una medida de seguridad adicional a la contraseña.

Su finalidad es proteger la cuenta de PRADO frente a accesos no autorizados.

No puede deshabilitarse, aunque la persona puede utilizar el correo electrónico en lugar de una aplicación de autenticación cuando esa opción esté disponible.

## Cuándo aplicar este procedimiento

Aplicar cuando la persona indique, por ejemplo:

- que el código generado por la aplicación no funciona;
- que el código aparece como incorrecto;
- que no puede completar la lectura del código QR;
- que el proceso de configuración ha quedado bloqueado;
- que ha cambiado o borrado la aplicación de autenticación;
- que ya configuró el 2FA, pero continúa viendo el aviso;
- que puede acceder a Grado, pero no a Posgrado, o al contrario;
- que solicita no utilizar la doble autenticación.

## Datos que hay que solicitar

Obtener los siguientes datos:

- nombre y apellidos;
- correo electrónico institucional;
- plataforma afectada:
  - PRADO Grado;
  - PRADO Posgrado;
  - ambas;
- mensaje de error exacto;
- fase en la que se produce el problema:
  - lectura del QR;
  - introducción del código;
  - acceso posterior;
- método utilizado:
  - aplicación de autenticación;
  - correo electrónico;
- sistema operativo del móvil:
  - Android;
  - iOS;
- indicación de si ya había configurado anteriormente el 2FA;
- captura de pantalla, cuando sea posible.

## Comprobaciones iniciales

### 1. Confirmar la plataforma afectada

La configuración del doble factor debe realizarse por separado en:

- PRADO Grado;
- PRADO Posgrado.

Que esté configurado en una plataforma no significa que también lo esté en la otra.

### 2. Comprobar el código utilizado

Si PRADO indica que el código es incorrecto, comprobar:

- que se está introduciendo el código más reciente;
- que no se utiliza un código anterior;
- que el código no ha caducado;
- que se escribe antes de que cambie en la aplicación;
- que la aplicación corresponde al registro correcto de PRADO.

### 3. Comprobar la hora automática del dispositivo

Una hora incorrecta en el móvil puede provocar que el código generado no coincida con el esperado.

Comprobar que está activada la configuración automática:

#### Android

```text
Ajustes → Fecha y hora → Fecha y hora automáticas
```

#### iOS

```text
Ajustes → General → Fecha y hora → Ajuste automático
```

### 4. Comprobar si la configuración ya es correcta

Cuando el sistema indique que el 2FA está correctamente configurado, el aviso del periodo de gracia puede seguir apareciendo hasta que finalice el plazo mostrado en la plataforma.

La aparición temporal de ese mensaje no implica necesariamente que la configuración haya fallado.

### 5. Comprobar la opción de recuerdo

Durante la activación puede aparecer una opción marcada para no volver a solicitar el código durante un periodo de hasta 30 días.

La disponibilidad y el texto exacto deben comprobarse en la pantalla mostrada a la persona usuaria.

## Árbol de decisión

### Caso 1. El código aparece como incorrecto

1. pedir que utilice únicamente el código más reciente;
2. comprobar que no ha caducado;
3. activar la hora automática del móvil;
4. volver a generar e introducir el código;
5. mantener la categoría `Acceso`.

### Caso 2. No puede completar el código QR

1. comprobar que se está configurando la plataforma correcta;
2. activar la hora automática;
3. eliminar de la aplicación los registros anteriores que correspondan a una configuración fallida;
4. restablecer el proceso de doble autenticación cuando proceda;
5. iniciar nuevamente la configuración;
6. seguir el tutorial disponible en la página principal de PRADO.

### Caso 3. El proceso está bloqueado

El bloqueo puede producirse después de varios intentos sin consignar correctamente la clave de seguridad.

Cuando se confirme:

1. restablecer el proceso de doble autenticación de la cuenta;
2. informar a la persona de que debe configurarlo nuevamente;
3. indicar que siga el tutorial de la plataforma;
4. pedir que concentre la información del problema en el mismo ticket.

### Caso 4. Ya está configurado, pero continúa el aviso

1. comprobar en el sistema que el 2FA está configurado correctamente;
2. informar de que el mensaje desaparecerá cuando finalice el periodo de gracia mostrado;
3. no restablecer la configuración si no existe otro error.

### Caso 5. No desea utilizar una aplicación

1. explicar que la doble autenticación no puede deshabilitarse;
2. informar de la posibilidad de utilizar el correo electrónico como alternativa, cuando aparezca disponible;
3. explicar la opción de recordar la verificación durante el periodo indicado.

### Caso 6. Funciona en Grado, pero no en Posgrado

1. comprobar qué plataforma está afectada;
2. recordar que la configuración se realiza por separado;
3. restablecer únicamente la plataforma que presenta el problema cuando proceda;
4. pedir que complete la configuración en esa plataforma.

### Caso 7. El problema continúa después del restablecimiento

1. solicitar el mensaje de error y una captura;
2. comprobar la plataforma y el correo;
3. confirmar la hora automática;
4. verificar que no utiliza un registro anterior de la aplicación;
5. revisar el caso como una incidencia de [Acceso](/prado/iris/acceso.md).

## Actuación técnica

Cuando proceda restablecer el 2FA:

1. confirmar la identidad de la persona;
2. identificar la plataforma afectada;
3. comprobar que se actúa sobre la cuenta correcta;
4. restablecer el proceso de doble autenticación;
5. registrar en el ticket:
   - cuenta afectada;
   - plataforma;
   - motivo del restablecimiento;
   - fecha de la actuación;
   - resultado comunicado;
6. pedir que la persona configure nuevamente el sistema siguiendo el tutorial de PRADO.

## Resultado esperado

La persona debe poder:

- completar la configuración del 2FA;
- generar un código válido;
- acceder a la plataforma correspondiente;
- distinguir la configuración de Grado y Posgrado;
- utilizar el método alternativo disponible cuando no emplee una aplicación.

## Clasificación en IRIS

La categoría habitual es:

- [Acceso](/prado/iris/acceso.md).

No utilizar `Incidencia administrativa` salvo que se compruebe que el expediente está bloqueado por una causa administrativa.

## Plantillas de respuesta

### Plantilla 1. Código incorrecto

Estimada/o [nombre]:

Si aparece un mensaje indicando que el código es incorrecto, compruebe lo siguiente:

- utilice únicamente el código más reciente;
- introdúzcalo antes de que caduque;
- active la hora automática de su dispositivo.

En Android:

```text
Ajustes → Fecha y hora → Fecha y hora automáticas
```

En iOS:

```text
Ajustes → General → Fecha y hora → Ajuste automático
```

Después, vuelva a generar e introducir el código.

Un saludo.

---

### Plantilla 2. Proceso restablecido

Estimada/o [nombre]:

Hemos restablecido el proceso de doble autenticación de su cuenta en [PRADO Grado/PRADO Posgrado].

Antes de configurarlo nuevamente, elimine de la aplicación los registros anteriores que correspondan a la configuración fallida y compruebe que su móvil tiene activada la hora automática.

A continuación, siga los pasos del tutorial disponible en la página principal de la plataforma.

Un saludo.

---

### Plantilla 3. Configuración correcta y aviso visible

Estimada/o [nombre]:

Hemos comprobado que tiene correctamente configurado el doble factor de autenticación.

El aviso que continúa apareciendo corresponde al periodo de gracia y desaparecerá cuando finalice el plazo indicado en la propia plataforma.

Un saludo.

---

### Plantilla 4. No puede deshabilitarse

Estimada/o [nombre]:

La doble autenticación es una medida de seguridad adicional a la contraseña y no es posible deshabilitarla.

No obstante, puede utilizar el correo electrónico en lugar de una aplicación de autenticación cuando la plataforma le ofrezca esa opción.

También puede aparecer una opción para no volver a introducir el código durante el periodo indicado.

Un saludo.

---

### Plantilla 5. Grado y Posgrado

Estimada/o [nombre]:

La doble autenticación debe configurarse de forma independiente en PRADO Grado y PRADO Posgrado.

Que esté activada en una plataforma no implica que también lo esté en la otra.

Hemos restablecido el proceso correspondiente a [plataforma] para que pueda configurarlo nuevamente.

Un saludo.

## Conceptos relacionados

- [Proveedor de identidad —IdP—](/prado/conceptos-y-reglas/proveedor-identidad-idp.md)
- [Consulta de Estado para Acceso a PRADO en Oficina Virtual](/prado/conceptos-y-reglas/consulta-estado-acceso-prado.md)

## Categorías de IRIS relacionadas

- [Acceso](/prado/iris/acceso.md)
- [Incidencia administrativa](/prado/iris/incidencia-administrativa.md)

## Procedimientos relacionados

- [Comprobación del estado de acceso](/prado/procedimientos/comprobacion-estado-acceso.md)
- [Acceso de un docente externo](/prado/procedimientos/acceso-docente-externo.md)
