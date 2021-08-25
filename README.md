## SHS Docs

Documentación apps Si Hay Sistema

# Instalación

## Requisitos
- ERPNext y Frappe V13+
- Wiki App

### Instalación app wiki
> App es un fork de [wiki](https://github.com/frappe/wiki) de frappe, para funcionar en version-13. Hasta que oficialmente este disponible para la rama estable.

**Obtén el app**

```bash
bench get-app --branch shs-docs https://github.com/sihaysistema/wiki.git
```

**Instala**
```bash
bench install-app wiki
```

## Instalación app shs-docs
**Obtén el app**

```bash
bench get-app https://github.com/sihaysistema/shs-docs.git
```

**Instala**
```bash
bench install-app shs_docs
```

## Migración fixtures y construcción de assets
```bash
bench migrate && bench build
```

## Desinstalar apps
> NOTA: Algunos campos puede quedar en base de datos esto no afectará al funcionamiento del ERP.

```bash
bench uninstall-app revelare
```

y

```bash
bench remove-from-installed-apps revelare
```

#### License

MIT